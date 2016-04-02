class Log:

    def __init__(self):
        self.id = None
        self.resource_id = None
        self.role_id = None
        self.info = None
        self.timestamp = None

    def get_id(self):
        return self.id

    def get_resource_id(self):
        return self.resource_id

    def get_role_id(self):
        return self.role_id

    def get_info(self):
        return self.info

    def get_timestamp(self):
        return self.timestamp

    def set_id(self,id):
        self.id = id

    def set_resource_id(self, resource_id):
        self.resource_id = resource_id

    def set_role_id(self, role_id):
        self.role_id = role_id

    def set_info(self, info):
        self.info = info

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp


