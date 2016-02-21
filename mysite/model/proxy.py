from datetime import datetime

from mysite.model.device import Device

class Proxy():

    id = None
    name = None
    description = None
    last_connected = None
    mac_address = None
    ip_address = None
    model = None
    os = None
    devices = []
    DATETIME_FORMAT = "%Y/%m/%d %H:%M"

    def __init__(self):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_last_connected(self):
        return self.last_connected

    def get_mac_address(self):
        return self.mac_address

    def get_ip_address(self):
        return self.ip_address

    def get_model(self):
        return self.model

    def get_os(self):
        return self.os

    def get_devices(self):
        return self.devices

    def set_id(self,id):
        self.id = id
        return self

    def set_name(self,name):
        self.name = name
        return self

    def set_description(self,description):
        self.description = description
        return self

    def set_last_connected(self,last_connected):
        self.last_connected = last_connected
        return self

    def set_mac_address(self,mac_address):
        self.mac_address = mac_address
        return self

    def set_ip_address(self,ip_address):
        self.ip_address = ip_address
        return self

    def set_model(self,model):
        self.model = model
        return self

    def set_os(self,os):
        self.os = os
        return self

    def set_devices(self,devices):
        self.devices = devices
        return self

    def add_device(self,device):
        self.devices.append(device)

    def remove_device(self,device):
        try:
            self.devices.remove(device)
            return True
        except Exception as e:
            return False

    def clear_devices(self):
        self.devices = []

    def toJSON(self):
        result = {
                "id"             : self.id,
                "name"           : self.name,
                "description"    : self.description,
                "last_connected" : self.last_connected.strftime(self.DATETIME_FORMAT),
                "mac_address"    : self.mac_address,
                "ip_address"     : self.ip_address,
                "model"          : self.model,
                "os"             : self.os,
                "devices"        : []
            }

        for device in self.devices:
            result.get('devices').append(device.toJSON())

        return result

    @staticmethod
    def fromJSON(json_data):
        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            proxy = Proxy()
            proxy.clear_devices()

            proxy.set_id(json_data.get("id",None))
            proxy.set_name(json_data.get("name",None))
            proxy.set_description(json_data.get("description",None))
            proxy.set_last_connected(json_data.get("last_connected",None))
            proxy.set_mac_address(json_data.get("mac_address",None))
            proxy.set_ip_address(json_data.get("ip_address",None))
            proxy.set_model(json_data.get("model",None))
            proxy.set_os(json_data.get("os",None))


            for device_data in json_data.get("devices"):
                device = Device.fromJSON(device_data)
                proxy.add_device(device)

            return proxy

        return None
