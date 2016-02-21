
class Group():

    GROUP_PROXY = "PROXY"
    GROUP_ENTITY = "ENTITY"

    id = None
    name = None
    description = None
    group_for = None
    members = []

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.decription

    def get_group_for(self):
        return self.group_for

    def get_members(self):
        return self.members

    def set_id(self,id):
        self.id = id
        return self

    def set_name(self,name):
        self.name = name
        return self

    def set_description(self,description):
        self.description = description
        return self

    def set_group_for(self,group_for):
        self.group_for = group_for
        return self

    def set_members(self,members):
        self.members = members
        return self

    def add_member(self,member):
        self.members.append(member)

    def remove_member(self,member):
        try:
            self.members.remove(member)
            return True
        except Exception as e:
            return False

    def clear_members(self):
        self.members = []

    def toJSON(self):

        result = {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "group_for" : self.group_for,
                "members" : []
            }

        for member in self.members:
            result.get('members').append(member)

        return result

    @staticmethod
    def fromJSON(json_data):

        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            group = Group()

            group.set_id(json_data.get("id",None))
            group.set_name(json_data.get("name",None))
            group.set_description(json_data.get("description",None))
            group.set_group_for(json_data.get("group_for",None))
            group.set_members(json_data.get("members",None))

            return group

        return None
