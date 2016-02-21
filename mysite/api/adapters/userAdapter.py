# -*- coding: utf-8 -*-

from mysite.model.user import User
from mysite.model.role import Role
from hashlib import sha1
import uuid

class UserAdapter:

    salt = "seskbum"
    cursor = None
    deviceAdapter = None

    def __init__(self, cursor):
        self.cursor = cursor

    def __del__(self):
        pass

    def sign_in(self,credentials):

        username = credentials.get("username")
        password = credentials.get("password")

        pass_salt = (password + self.salt).encode('utf-8')

        hash = sha1()
        hash.update(pass_salt)

        query = "SELECT id from user where name= '%s' and password = '%s'" % (username,hash.hexdigest())

        self.cursor.execute(query)
        id = self.cursor.fetchone()

        if id is None:
            raise ValueError("User not found")

        user = self.get_by_id(id)
        return user

    def register(self,user_data):
        # password - ahoj
        # user - test

        username = user_data.get("username")
        password = user_data.get("password")
        role = user_data.get("role")

        pass_salt = (password + self.salt).encode('utf-8')

        hash = sha1()
        hash.update(pass_salt)

        id = str(uuid.uuid1())

        query = "INSERT INTO user (id, name, password, role) VALUES \
                ('%s','%s','%s','%s') " % (
                   id, username ,hash.hexdigest(), role)

        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e


    def get_by_id(self,id):

        query = "SELECT * FROM user where id='%s'" % id

        self.cursor.execute(query)
        row = self.cursor.fetchone()

        user = self.create(row)
        return user

    def set_role(self, role_id):

        query = "SELECT * FROM role where id = '%s'" % role_id

        self.cursor.execute(query)
        row = self.cursor.fetchone()

        role = Role()
        role.set_id(row[0])
        role.set_name(row[1])
        role.set_description(row[2])

        return role

    def logout(user):
        pass

    def create(self,row):

        user = User()
        user.set_id(row[0])
        user.set_name(row[2])
        user.set_role(self.set_role(row[1]))

        return user


