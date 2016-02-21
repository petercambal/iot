from datetime import datetime

class Device():

    id = None
    name = None
    proxy_id = None
    last_connected = None
    DATETIME_FORMAT = "%Y/%m/%d %H:%M"

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_proxy_id(self):
        return self.proxy_id

    def get_last_connected(self):
        return self.last_connected

    def set_id(self,id):
        self.id = id
        return self

    def set_name(self,name):
        self.name = name
        return self

    def set_proxy_id(self,proxy_id):
        self.proxy_id = proxy_id
        return self

    def set_last_connected(self,last_connected):
        self.last_connected = last_connected
        return self

    def toJSON(self):
        return {
                "id"             : self.id,
                "name"           : self.name,
                "proxy_id"       : self.proxy_id,
                "last_connected" : self.last_connected.strftime(self.DATETIME_FORMAT)
            }

    @staticmethod
    def fromJSON(json_data):
        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            device = Device()
            device.set_id(json_data.get("id",None))
            device.set_name(json_data.get("name",None))
            device.set_proxy_id(json_data.get("proxy_id",None))
            device.set_last_connected(json_data.get("last_connected",None)) # mozno bude treba pridat konverziu na datetime

            return device

        return None
