#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysite.api.adapters.virtualEntityAdapter import VirtualEntityAdapter

class VirtualEntityService:

    db = None

    def __init__(self,db):
        self.db = db

    def get(self):
        entityAdapter = VirtualEntityAdapter(self.db)
        entities = entityAdapter.getAll()

        result = []
        for entity in entities:
            result.append(entity.toJSON())
        return result

    def set(self):
       pass

    def delete(self):
       pass



