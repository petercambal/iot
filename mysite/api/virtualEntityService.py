#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysite.api.adapters.virtualEntityAdapter import VirtualEntityAdapter
from mysite.api.adapters.domainAdapter import DomainAdapter
from mysite.api.services.dbservice import DB
import re

class VirtualEntityService:

    db = None
    cursor = None
    re_uuid = re.compile(r'(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})')
    re_url = re.compile(r'(?P<url>([\d\w\-]+\/)*([\d\w\-]+){1})')

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = self.db.cursor()
        print("EntityService - Opening")

    def __del__(self):
        if self.db:
            print("EntityService - Closing")
            self.db.close()

    def get(self,request_url):
        entityAdapter = VirtualEntityAdapter(self.cursor)
        domainAdapter = DomainAdapter(self.cursor)
        id = None
        path = None

        if re.match(self.re_uuid,request_url):
            id = re.search(self.re_uuid, request_url).group('uuid')
            entity = entityAdapter.getById(id)
            return entity.toJSON()

        elif re.match(self.re_url,request_url):
            top_level_domain_id = domainAdapter.get_top_level_domain().get_id()
            path = re.search(self.re_url,request_url).group('url')
            domains = path.split('/')
            parent_id = top_level_domain_id
            name = domains.pop()
            for domain in domains:
                domain = domainAdapter.find_domain(domain,parent_id)
                if domain:
                    parent_id = domain.get_id()
                else:
                    return None

            entity = entityAdapter.get_by_domain_id_entity_name(parent_id,name)
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

    def set(self):
       pass

    def delete(self):
       pass


