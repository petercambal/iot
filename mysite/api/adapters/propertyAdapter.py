# -*- coding: utf-8 -*-

from mysite.model.property import Property
from mysite.api.adapters.deviceAdapter import DeviceAdapter


class PropertyAdapter:
    cursor = None

    def __init__(self, cursor):
        self.cursor = cursor
        self.deviceAdapter = DeviceAdapter(self.cursor)

    def __del__(self):
        pass

    def getById(self, id):

        query = "SELECT * FROM property WHERE id ='%s'" % (id)
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        property = self.create(row)

        return property

    def getByName(self, name):

        query = "SELECT * FROM property WHERE name ='%s'" % (name)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        properties_list = []
        for row in rows:
            property = self.create(row)
            properties_list.append(property)

        return properties_list

    def getByNameLike(self, name):
        pass

    def getAll(self):
        pass

    def getByEntityId(self, entity_id):

        query = "SELECT * FROM property WHERE entity_id ='%s'" % (entity_id)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        properties_list = []
        for row in rows:
            property = self.create(row)
            properties_list.append(property)

        return properties_list

    def getByEntityDevice(self, property):

        query = "SELECT * FROM property WHERE entity_id = '%s' AND device_id = '%s'" % (
            property.get_entity_id(),
            property.get_device_id()
        )

        self.cursor.execute(query)
        row = self.cursor.fetchone()
        property = self.create(row)

        return property


    def insert(self, property):

        query = "INSERT INTO property (id,name,entity_id,device_id) VALUES \
			 ('%s','%s','%s','%s')" % (
            property.get_id(),
            property.get_name(),
            property.get_entity_id(),
            property.get_device_id()
        )
        try:
            self.cursor.execute(query)

        except Exception as e:

            raise e

    def update(self, property):
        query = "UPDATE propery SET name='%s', entity_id='%s', device_id='%s' WHERE id= '%s'" % (
            property.get_name(),
            property.get_entity_id(),
            property.get_device_id(),
            property.get_id()
        )

        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def inline_update(self, id, column, value):

        query = "UPDATE property SET %s = '%s' where id ='%s' " % (
            column,
            value,
            id
        )

        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def delete(self, id):

        query = "DELETE FROM property WHERE id = '%s' " % (id)
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def deleteByEntityId(self, entity_id):
        query = "DELETE from property WHERE entity_id = '%s'" % (entity_id)
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def create(self, row):

        try:
            property = Property()
            property.set_id(row[0])
            property.set_name(row[1])
            property.set_entity_id(row[2])
            property.set_device_id(row[3])
            property.set_device(self.deviceAdapter.get_by_id(row[3]))

            return property

        except:
            return None
