#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysite.api.adapters.proxyAdapter import ProxyAdapter
from mysite.api.adapters.deviceAdapter import DeviceAdapter
from mysite.api.adapters.virtualEntityAdapter import VirtualEntityAdapter
from mysite.api.adapters.propertyAdapter import PropertyAdapter
from mysite.api.adapters.connectOptionAdapter import ConnectOptionsAdapter
from mysite.model.proxy import Proxy
from mysite.model.virtualEntity import VirtualEntity
from mysite.model.property import Property
from mysite.api.services.dbservice import DB
#import paho.mqtt.client as mqtt

class ProxyService:

    db = None
    cursor = None

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = self.db.cursor()

    def __del__(self):
        if self.db:
            self.db.close()

    def get(self,request):
        proxyAdapter = ProxyAdapter(self.cursor)

        proxies = proxyAdapter.get_all()

        result = []
        for proxy in proxies:
            result.append(proxy.toJSON())
        return result

    def set(self,data):
        proxyAdapter = ProxyAdapter(self.cursor)
        deviceAdapter = DeviceAdapter(self.cursor)
        entityAdapter = VirtualEntityAdapter(self.cursor)
        propertyAdapter = PropertyAdapter(self.cursor)
        connectOptionAdapter = ConnectOptionsAdapter(self.cursor)

        try:
            # create proxy object
            proxy = Proxy.fromJSON(data)
            if not proxy:
                raise ValueError('Failed creating proxy')

            # if proxy is registered, update last_connected timestamp
            if proxyAdapter.proxy_exists(proxy):

                proxyAdapter.update_timestamp(proxy)

                for device in proxy.get_devices():
                    if deviceAdapter.device_exists(device):
                        deviceAdapter.update_timestamp(device)
                    else:
                        deviceAdapter.insert(device)
                        #TODO: add to virtualEntity new property based on device
                        property_data = {
                                    "name" : device.get_name(),
                                    "device_id" : device.get_id(),
                                    "entity_id" : data.get("entity_id")
                            }
                        property = Property.fromJSON(property_data)
                        propertyAdapter.insert(property)

                        for connect_option in device.get_connect_options():
                            connectOptionAdapter.insert(connect_option, device.get_id())

            # else insert record to db and create virtual entity + properties
            else:
                proxyAdapter.insert(proxy)
                for device in proxy.get_devices():
                    deviceAdapter.insert(device)
                    for connect_option in device.get_connect_options():
                        connectOptionAdapter.insert(connect_option, device.get_id())

                # automatically create virtual entity based on prxy data
                # TODO: Domain Id
                entity_id = data.get("entity_id")
                # domain_id = entityAdapter.get_domain_id_for_entity()
                entity_data = {
                            "id" : entity_id,
                            "name": proxy.get_name(),
                            "description": proxy.get_description(),
                            "domain_id" : "1ee79924-ccf1-11e5-964a-22000b95cd49",
                            "properties" : []
                    }

                for device in proxy.get_devices():
                    entity_data.get("properties").append({
                            "name" : device.get_name(),
                            "entity_id" : entity_id,
                            "device_id" : device.get_id()
                        })

                entity = VirtualEntity.fromJSON(entity_data)
                entityAdapter.insert(entity)

                for property in entity.get_properties():
                    propertyAdapter.insert(property)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def put(self,data):
        proxyAdapter = ProxyAdapter(self.cursor)
        deviceAdapter = DeviceAdapter(self.cursor)
        try:
            proxy = Proxy.fromJSON(data)
            if not proxy:
                raise ValueError('Failed updating proxy')
            proxyAdapter.update(proxy)

            for device in proxy.get_devices():
                deviceAdapter.update(device)

            #mqttc = mqtt.Client()
            #mqttc.publish('config/%s' % proxy.get_name(), data, qos = 1, retain = True)

            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e


    def delete(self,id):
        try:
            proxyAdapter = ProxyAdapter(self.cursor)
            proxyAdapter.delete(id)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

