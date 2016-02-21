#!/usr/bin/python
# -*- coding: utf-8 -*-

class DomainService:

    # class handling proxy database operations

    db = None
    cursor = None

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    # return id of top level domain
    def get_tld_id(self):
        query = "SELECT id FROM domain WHERE parent_id is NULL"
        self.cursor.execute(query)
        id = self.cursor.fetchone()[0]
        return id

    def find_domain(self,name,parent):
        query = "SELECT id FROM domain WHERE name='%s' and parent_id = '%s'" % (name,parent)
        self.cursor.execute(query)
        id = self.cursor.fetchone()[0]
        return id

    #get method
    def getProxy(self,id=None):
        if id == None:
            query = "SELECT * FROM proxy"
        else:
            query = "SELECT * FROM proxy WHERE id='%s'" % (id)

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            result_list = []
            for row in rows:
                p = {}
                p['id'] = row[0]
                p['name'] = row[1]
                p['description'] = row[2]
                p['last_connected'] = str(row[3])
                p['mac_address'] = row[4]
                p['ip_address'] = row[5]
                p['model'] = row[6]
                p['os'] = row[7]
                result_list.append(p)
            return result_list
        except Exception as e:
            return {'result' : False , 'message' : e}

    #delete method
    def deleteProxy(self,id):
        query = "DELETE FROM proxy WHERE id = '%s' " % (id)
        try:
            self.cursor.execute(query)
            self.db.commit()
            return {'result' : True}
        except Exception as e:
            self.db.rollback()
            return {'result' : False}


    def insertProxy(self,data):

    # proxy not found

        query = "INSERT INTO proxy (id,name,description,last_connected,mac_address,ip_address,model,os) VALUES \
			 ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
            data['id'],
            data['name'],
            data['description'],
            data['time'],
            data['mac'],
            data['ip'],
            data['model'],
            data['os'],
            )
        try:
            self.cursor.execute(query)
            self.db.commit()
            return {'result' : True}
        except Exception as e:
            self.db.rollback()
            return {'result' : False}

    def updateProxy(self,time,mac):

    # proxy found - update

        query = "UPDATE proxy set last_connected = '%s' where mac_address = '%s' " % (time, mac)
        try:
            self.cursor.execute(query)
            self.db.commit()
            return {'result' : True}
        except Exception as e:
            self.db.rollback()
            return {'result' : False}

