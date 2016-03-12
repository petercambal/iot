#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysite.api.services.dbservice import DB
from mysite.api.adapters.deviceAdapter import DeviceAdapter

class DeviceService:

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

    def set(self,data):
        device_adapter = DeviceAdapter(self.cursor)
        try:
            # name is name of column in db
            name = data.get('name',None)
            id = data.get('pk',None)
            value = data.get('value',None)

            if name and id and value:
                if name == "name":
                    device_adapter.update_name(id,value)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
