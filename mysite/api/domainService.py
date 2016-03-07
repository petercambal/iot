#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysite.api.services.dbservice import DB

class DomainService:

    # class handling proxy database operations

    db = None
    cursor = None

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = db.cursor()
        print("DomainService - Opening")

    def __del__(self):
        if self.db:
            self.db.close()
            print("DomainService - Closing")

