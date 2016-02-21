# -*- coding: utf-8 -*-
from mysite.model.virtualEntity import VirtualEntity
from mysite.api.adapters.propertyAdapter import PropertyAdapter

class VirtualEntityAdapter():

    cursor = None
    propertyAdapter = None

    def __init__(self,cursor):
        self.cursor = cursor
        self.propertyAdapter = PropertyAdapter(self.cursor)

    def __del__(self):
        pass

    def getById(self,id):

        query = "SELECT * FROM virtualEntity WHERE id = '%s'" % (id)
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        entity = self.create(row)

        return entity


    def getAll(self):

        query = "SELECT * FROM virtualEntity"

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        entities_list = []

        for row in rows:
             entity = self.create(row)
             entities_list.append(entity)

        return entities_list

    def get_by_domain_id(self,domain_id):

        query = "SELECT * FROM virtualEntity where domain_id = '%s'" %(domain_id)

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        entities_list = []

        for row in rows:
            entity = self.create(row)
            entities_list.append(entity)

        return entities_list

    def get_by_ids(self,ids):

        query = "SELECT * FROM virtualEntity where id in("

        for id in ids:
            if id is ids[-1]:
                query +=  "'%s'" % id
            else:
                query += "'%s'," % id

        query+= ")"

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        entities_list = []

        for row in rows:
            entity = self.create(row)
            entities_list.append(entity)

        return entities_list

    def get_by_condition(self,ids,condition):
        pass

    def insert(self,entity):

        query = "INSERT INTO virtualEntity (id,name,description,domain_id) VALUES \
			 ('%s','%s','%s','%s')" % (
            entity.get_id(),
            entity.get_name(),
            entity.get_description(),
            entity.get_domain_id()
            )

        try:
            self.cursor.execute(query)
        except Exception as e:

            raise e

    def update(self,entity):

        query = "UPDATE virtualEntity SET name='%s', description='%s', domain_id='%s' WHERE id='%s'" % (
            entity.get_name(),
            entity.get_description(),
            entity.get_domain_id(),
            entity.get_id()
            )
        try:
            self.cursor.execute(query)

        except Exception as e:

            raise e


    def delete (self,entity):

        query = "DELETE FROM virtualEntity WHERE id = '%s' " % (id)
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def create(self,row):

        entity = VirtualEntity()
        entity.set_id(row[0])
        entity.set_name(row[1])
        entity.set_description(row[2])
        entity.set_domain_id(row[3])

        entity.set_properties(self.propertyAdapter.getByEntityId(row[0]))

        return entity


