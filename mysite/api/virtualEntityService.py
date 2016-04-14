#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysite.model.virtualEntity import VirtualEntity
from mysite.api.adapters.virtualEntityAdapter import VirtualEntityAdapter
from mysite.api.adapters.domainAdapter import DomainAdapter
from mysite.api.adapters.propertyAdapter import PropertyAdapter
from mysite.api.services.dbservice import DB
from mysite.model.log import Log
from mysite.api.adapters.logAdapter import LogAdapter
import re
from uuid import uuid1
import datetime


class VirtualEntityService:
    db = None
    cursor = None
    re_uuid = re.compile(r'(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})')
    re_url = re.compile(r'(?P<url>([\d\w\-]+\/)*([\d\w\-]+){1})')

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = self.db.cursor()

    def __del__(self):
        if self.db:
            self.db.close()

    def get(self, request_url):
        entityAdapter = VirtualEntityAdapter(self.cursor)
        domainAdapter = DomainAdapter(self.cursor)
        id = None
        path = None

        self.log_request()

        if re.match(self.re_uuid, request_url):
            id = re.search(self.re_uuid, request_url).group('uuid')
            print("ve start")
            print(datetime.datetime.now())
            entity = entityAdapter.getById(id)
            print(datetime.datetime.now())
            print("ve end")
            return entity.toJSON()

        elif re.match(self.re_url, request_url):
            top_level_domain_id = domainAdapter.get_top_level_domain().get_id()
            path = re.search(self.re_url, request_url).group('url')
            domains = path.split('/')
            parent_id = top_level_domain_id
            name = domains.pop()
            for domain in domains:
                domain = domainAdapter.find_domain(domain, parent_id)
                if domain:
                    parent_id = domain.get_id()
                else:
                    return None

            entity = entityAdapter.get_by_domain_id_entity_name(parent_id, name)
            if entity:
                return entity.toJSON()
            else:
                return None

        elif request_url == "":
            entities = entityAdapter.getAll()

            result = []
            for entity in entities:
                result.append(entity.toJSON())
            return result

    def put(self, data):
        entity_adapter = VirtualEntityAdapter(self.cursor)
        try:

            source = data.get('source')

            if source == "inline":

                id = data.get("pk", None)
                column = data.get("name", None)
                value = data.get("value", None)

                if id and column and value:
                    if column.startswith("entity"):
                        if "name" in column:
                            column = "name"
                        elif "description" in column:
                            column = "description"

                        entity_adapter.inline_update(id, column, value)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def set(self, data):
        entity_adapter = VirtualEntityAdapter(self.cursor)
        property_adapter = PropertyAdapter(self.cursor)
        try:
            entity = VirtualEntity.fromJSON(data)

            if entity:
                entity_adapter.insert(entity)

                for property in entity.get_properties():
                    property_adapter.insert(property)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e


    def delete(self, id):
        entity_adapter = VirtualEntityAdapter(self.cursor)
        property_adapter = PropertyAdapter(self.cursor)
        try:
            property_adapter.deleteByEntityId(id)
            entity_adapter.delete(id)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def log_request(self):
        try:
            logAdapter = LogAdapter(self.cursor)
            log = Log()
            log.set_id(uuid1().hex)
            log.set_resource_id("d1cdb926-c54e-11e5-89ba-22000b79ceab")
            log.set_role_id("78c631a2-c54c-11e5-89ba-22000b79ceab")

            logAdapter.insert(log)
            self.db.commit()
        except:
            pass



