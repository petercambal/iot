# -*- coding: utf-8 -*-

from mysite.model.proxy import Proxy
from mysite.api.adapters.deviceAdapter import DeviceAdapter

class ProxyAdapter:

    cursor = None
    deviceAdapter = None

    def __init__(self, cursor):
        self.cursor = cursor
        self.deviceAdapter = DeviceAdapter(cursor)

    def __del__(self):
        pass

    def getById(self,id):

        query = "SELECT * FROM proxy where id = '%s'" % (id)
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        proxy = self.create(row)
        return proxy

    def get_all(self):

        query = "SELECT * FROM proxy"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        proxies = []
        for row in rows:
            proxy = self.create(row)
            proxies.append(proxy)

        return proxies

    def insert(self,proxy):

        query = "INSERT INTO proxy (id,name,description,mac_address,ip_address,model,os) VALUES \
			 ('%s','%s','%s','%s','%s','%s','%s')" % (
            proxy.get_id(),
            proxy.get_name(),
            proxy.get_description(),
            proxy.get_mac_address(),
            proxy.get_ip_address(),
            proxy.get_model(),
            proxy.get_os()
            )
        print(query)
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def update(self,proxy):

        query = "UPDATE proxy set last_connected = CURRENT_TIMESTAMP() where mac_address = '%s' " % (
            proxy.get_mac_address()
            )
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def proxy_exists(self,proxy):
         self.cursor.execute("SELECT count(*) from proxy where mac_address = '%s'" % proxy.get_mac_address())
         count = self.cursor.fetchone()[0]

         if count is 0:
            return False
         else:
            return True


    def delete(self, id):

        query = "DELETE FROM proxy WHERE id = '%s' " % (id)
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def create(self,row):
        proxy = Proxy()
        proxy.set_id(row[0])
        proxy.set_name(row[1])
        proxy.set_description(row[2])
        proxy.set_last_connected(row[3])
        proxy.set_mac_address(row[4])
        proxy.set_ip_address(row[5])
        proxy.set_model(row[6])
        proxy.set_os(row[7])

        proxy.set_devices(self.deviceAdapter.get_by_proxy_id(row[0]))

        return proxy