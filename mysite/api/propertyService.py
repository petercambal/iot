#!/usr/bin/python
# -*- coding: utf-8 -*-

# from mysite.api.adapters import PropertyAdapter

from mysite.api.services.dbservice import DB

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

    def set(self):
       pass

    def delete(self):
       pass


