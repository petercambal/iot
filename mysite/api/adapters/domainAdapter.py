# -*- coding: utf-8 -*-
from mysite.model.domain import Domain

class DomainAdapter():

    cursor = None

    def __init__(self,cursor):
        self.cursor = cursor

    def __del__(self):
        pass

    def getById(self,id):

        query = "SELECT * FROM domain WHERE id= '%s'" % (id)
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        domain = self.create(row)
        return domain

    def insert(self,domain):

        query = "INSERT INTO domain (id,name,parent_id) VALUES \
                ('%s','%s','%s')" % (
                    domain.get_id(),
                    domain.get_name(),
                    domain.get_parent_id()
                    )
        try:
            self.cursor.execute(query)
        except Exception as e:
            self.db.rollback()
            raise e

    def update(self,domain):

        query = "UPDATE domain SET name= '%s', parent_id='%s' where id= '%s'" % (
                    domain.get_name(),
                    domain.get_parent_id(),
                    domain.get_id()
                )
        try:
            self.cursor.execute(query)
        except Exception as e:
            self.db.rollback()
            raise e

    def delete(self,id):

        query = "DELETE FROM domain WHERE id = '%s' " % (id)
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            self.db.rollback()

    def getTopLevelDomain(self):

        query = "SELECT * FROM domain WHERE parent_id is NULL"
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        domain = self.create(row)
        return domain

    def create(self,row):

        domain = Domain()
        domain.set_id(row[0])
        domain.set_name(row[1])
        domain.set_parent_id(row[2] if len(row) is 3 else None)

        return domain