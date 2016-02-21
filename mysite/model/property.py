import uuid

class Property():

    id = None
    name = None
    entity_id = None
    device_id = None

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_entity_id(self):
        return self.entity_id

    def get_device_id(self):
        return self.device_id

    def set_id(self,id):
        self.id = id
        return self

    def set_name(self,name):
        self.name = name
        return self

    def set_entity_id(self,entity_id):
        self.entity_id = entity_id
        return self

    def set_device_id(self,device_id):
        self.device_id = device_id
        return self

    def toJSON(self):
        return{
                "id"        : self.id,
                "name"      : self.name,
                "entity_id" : self.entity_id,
                "device_id" : self.device_id
                }

    @staticmethod
    def fromJSON(json_data):
        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            property = Property()
            property.set_id(json_data.get("id",str(uuid.uuid1())))
            property.set_name(json_data.get("name",None))
            property.set_entity_id(json_data.get("entity_id",None))
            property.set_device_id(json_data.get("device_id",None))

            return property

        return None
