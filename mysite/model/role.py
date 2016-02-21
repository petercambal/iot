import uuid

class Role():

    id = None
    name = None
    description = None

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_id(self, id):
        self.id = id

    def set_name(self,name):
        self.name = name

    def set_description(self,description):
        self.description = description

    def toJSON(self):
        return {
                "id" : self.id,
                "name" : self.name,
                "description" : self.description
            }

    def fromJSON(json_data):
        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            role = Role()
            role.set_id(json_data.get("id",str(uuid.uuid1())))
            role.set_name(json_data.get("name",None))
            role.set_description(json_data.get("description",None))

            return role

        return None
