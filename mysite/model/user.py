import uuid

from mysite.model.role import Role

class User():

    id = None    # string uuid
    name = None  # string
    role = None  # mysite.model.role

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role

    def set_id(self, id):
        self.id = id

    def set_name(self,name):
        self.name = name

    def set_role(self,role):
        self.role = role

    def toJSON(self):

        return {
                "id"   : self.id,
                "name" : self.name,
                "role" : self.role.toJSON()
            }

    @staticmethod
    def fromJSON(json_data):
        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            user = User()
            user.set_id(json_data.get("id",str(uuid.uuid1())))
            user.set_name(json_data.get("name",None))
            user.set_role(Role.fromJSON(json_data.get("role")),None)

            return user

        return None

