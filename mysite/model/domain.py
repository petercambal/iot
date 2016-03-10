from uuid import uuid1

class Domain():

    id = None
    name = None
    parent_id = None

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_parent_id(self):
        return self.parent_id

    def set_id(self,id):
        self.id = id
        return self

    def set_name(self, name):
        self.name = name
        return self

    def set_parent_id(self, parent_id):
        self.parent_id = parent_id
        return self

    def toJSON(self):
        return {
                "id"       : self.id,
                "name"     : self.name,
                "parent_id": self.parent_id
            }

    @staticmethod
    def fromJSON(json_data):
        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            domain = Domain()
            if json_data.get("id") == "":
                domain.set_id(str(uuid1()))
            else:
                domain.set_id(json_data.get("id"))
            domain.set_name(json_data.get("name",None))
            domain.set_parent_id(json_data.get("parent_id",None))

            return domain

        return None
