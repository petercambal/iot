#!/usr/bin/python
# -*- coding: utf-8 -*-

# from mysite.api.adapters import PropertyAdapter

from mysite.api.services.dbservice import DB
from mysite.api.adapters.propertyAdapter import PropertyAdapter
from mysite.model.property import Property

class PropertyService:

    db = None
    cursor = None

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = self.db.cursor()
        print("PropertyService - Opening")

    def __del__(self):
        if self.db:
            self.db.close()
            print("PropertyService - Closing")

    def get(self):
       pass

    def set(self, data):
        property_adapter = PropertyAdapter(self.cursor)

        try:
            entity_id = data.get('entity_id')

            if len(data.get('properties')) == 0:
                property_adapter.deleteByEntityId(entity_id)

            else:
                db_ids = []
                db_properties = property_adapter.getByEntityId(entity_id)

                for db_prop in db_properties:
                    db_ids.append(db_prop.get_id())

                req_ids = []
                for prop_json in data.get('properties'):
                    prop_json.update({'entity_id': entity_id})

                    property = Property.fromJSON(prop_json)
                    if property_adapter.getByEntityDevice(property):
                        req_ids.append(property.get_id())
                    else:
                        property_adapter.insert(property)

                for db_prop_id in db_ids:
                    if db_prop_id not in req_ids:
                        property_adapter.delete(db_prop_id)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e


    def put(self, data):
        property_adapter = PropertyAdapter(self.cursor)
        try:

            source = data.get('source')

            if source == "inline":

                id = data.get("pk", None)
                column = data.get("name", None)
                value = data.get("value", None)

                if id and column and value:
                    if column.startswith("property"):
                        if "name" in column:
                            column = "name"
                        elif "description" in column:
                            column = "description"

                        property_adapter.inline_update(id, column, value)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e


    def delete(self):
       pass


