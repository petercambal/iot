#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysite.api.services.dbservice import DB
from mysite.api.adapters.domainAdapter import DomainAdapter
from mysite.api.adapters.virtualEntityAdapter import VirtualEntityAdapter
from mysite.model.domain import Domain

class DomainService:

    # class handling proxy database operations

    db = None
    cursor = None

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = db.cursor()

    def __del__(self):
        if self.db:
            self.db.close()

    def get(self, id):
        domain_adapter = DomainAdapter(self.cursor)
        if id:
            entity_adapter = VirtualEntityAdapter(self.cursor)
            domain = domain_adapter.getById(id)
            entities = entity_adapter.get_by_domain_id(id)
            entities_result = []
            for entity in entities:
                entities_result.append(entity.toJSON())

            return {
                "domain": domain.toJSON(),
                "entities": entities_result
            }
        else:
            domains = domain_adapter.get_all()

            result = []
            for domain in domains:
                result.append(domain.toJSON())

            return result

    def set(self, data):
        domain_adapter = DomainAdapter(self.cursor)
        entity_adapter = VirtualEntityAdapter(self.cursor)

        try:
            method = data.get('method', None)
            if method:
                if method == "change_entity_domain":
                    entity_id = data.get('entity_id')
                    domain_id = data.get('domain_id')

                    if entity_id and domain_id:
                        entity_adapter.set_domain(entity_id, domain_id)
                    else:
                        raise ValueError("Entity or domain Id missing")

                else:
                    raise ValueError("Method not found")
            else:
                # insert or update
                id = data.get('id')
                domain = domain_adapter.getById(id)

                if domain:
                    domain.set_name(data.get('name', domain.get_name()))
                    domain.set_parent_id(data.get('parent_id', domain.get_parent_id()))
                    domain_adapter.update(domain)
                else:
                    domain = Domain().fromJSON(data)
                    domain_adapter.insert(domain)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
