from mysite.model.property import Property
import uuid

class VirtualEntity():

    id = None
    name = None
    description = None
    domain_id = None
    properties = []

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_domain_id(self):
        return self.domain_id

    def get_properties(self):
        return self.properties

    def set_id(self,id):
        self.id = id

    def set_name(self,name):
        self.name = name

    def set_description(self,description):
        self.description = description

    def set_domain_id(self,domain_id):
        self.domain_id = domain_id

    def add_property(self,property):
        self.properties.append(property)

    def set_properties(self,property_list):
        self.properties = property_list

    def remove_property(self,property):
        try:
            self.properties.remove(property)
            return True
        except Exception as e:
            return False

    def clear_properties(self):
        self.properties = []

    def toJSON(self):
        result = {
                "id" : self.id,
                "name" : self.name,
                "description" : self.description,
                "domain_id" : self.domain_id,
                "properties" : []
            }

        for property in self.properties:
            result.get('properties').append(property.toJSON())

        return result

    @staticmethod
    def fromJSON(json_data):
        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            entity = VirtualEntity()

            entity.set_id(json_data.get("id",str(uuid.uuid1())))
            entity.set_name(json_data.get("name",None))
            entity.set_description(json_data.get("description",None))
            entity.set_domain_id(json_data.get("domain_id",None))

            for property_data in json_data.get("properties"):
                property = Property.fromJSON(property_data)
                entity.add_property(property)

            return entity

        return None


