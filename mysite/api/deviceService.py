#!/usr/bin/python
# -*- coding: utf-8 -*-


class DeviceService:

    # class handling proxy database operations

    db = None
    cursor = None

    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    #get method
    def getDevice(self,id=None):
        if id == None:
            query = "SELECT * FROM device"
        else:
            query = "SELECT * FROM device WHERE id='%s'" % (id)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        result_list = []
        for row in rows:
            p = {}
            p['id'] = row[0]
            p['proxy_id'] = row[1]
            p['name'] = row[2]
            p['last_connected'] = str(row[3])
            result_list.append(p)
        return result_list

    #delete method
    def deleteProxy(self,id):
        query = "DELETE FROM device WHERE id = '%s' " % (id)
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            self.db.rollback()


    # post method
    def insertDevice(self,data):

        query = "INSERT INTO device (id,proxy_id,name) VALUES \
			 ('%s','%s','%s')" % (
            data['id'],
            data['proxyId'],
            data['name']
            )
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            self.db.rollback()

