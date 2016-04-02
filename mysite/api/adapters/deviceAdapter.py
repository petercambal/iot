# -*- coding: utf-8 -*-

from mysite.model.device import Device


class DeviceAdapter:
    cursor = None

    def __init__(self, cursor):
        self.cursor = cursor

    def __del__(self):
        pass

    def get_by_id(self, id):

        query = "SELECT * FROM device WHERE id = '%s'" % (id)
        self.cursor.execute(query)
        row = self.cursor.fetchone()

        device = self.create(row)
        return device

    def get_all(self):

        query = "SELECT * FROM device"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        devices = []
        for row in rows:
            device = self.create(row)
            devices.append(device)

        return devices

    def get_by_proxy_id(self, proxy_id):

        query = "SELECT * FROM device where proxy_id = '%s'" % (proxy_id)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        devices = []
        for row in rows:
            device = self.create(row)
            devices.append(device)

        return devices

    def insert(self, device):

        query = "INSERT INTO device (id,name,proxy_id) VALUES \
			 ('%s','%s','%s')" % (
            device.get_id(),
            device.get_name(),
            device.get_proxy_id()
        )
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def update(self, device):

        query = "UPDATE device SET name='%s', proxy_id='%s' WHERE id='%s'" % (

            device.get_name(),
            device.get_proxy_id(),
            device.get_id()
        )
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def update_timestamp(self, device):

        query = "UPDATE device SET last_connected= CURRENT_TIMESTAMP() WHERE id = '%s'" % (device.get_id())

        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def update_name(self, id, name):
        query = "UPDATE device set name='%s' where id = '%s'" % (name, id)

        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def device_exists(self, device):
        self.cursor.execute("SELECT count(*) from device where id = '%s'" % device.get_id())
        count = self.cursor.fetchone()[0]

        if count is 0:
            return False
        else:
            return True

    def delete(self, id):

        query = "DELETE FROM device WHERE id = '%s' " % (id)
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def delete_by_proxy_id(self, proxy_id):

        query = "DELETE FROM device WHERE proxy_id = '%s'" % (proxy_id)
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def create(self, row):
        device = Device()
        device.set_id(row[0])
        device.set_proxy_id(row[1])
        device.set_name(row[2])
        device.set_last_connected(row[3])
        device.set_topic(row[4])
        return device
