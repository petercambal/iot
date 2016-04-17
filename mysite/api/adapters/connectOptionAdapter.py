from mysite.model.connect_option import ConnectOption


class ConnectOptionsAdapter:
    cursor = None

    def __init__(self, cursor):
        self.cursor = cursor

    def __del__(self):
        pass

    def get_by_device(self, device_id):
        query = "SELECT * FROM connect_option WHERE device_id = '%s'" % device_id

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        connect_options = []
        for row in rows:
            connect_option = self.create(row)
            connect_options.append(connect_option)

        return connect_options

    def insert(self, connect_option, device_id):
        query = "INSERT INTO  connect_option (id,device_id,protocol, topic) VALUES  \
              ('%s','%s','%s','%s')" % (
            connect_option.get_id(),
            device_id,
            connect_option.get_protocol(),
            connect_option.get_topic()
        )
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def create(self, row):
        connect_option = ConnectOption()

        connect_option.set_id(row[0])
        connect_option.set_protocol(row[2])
        connect_option.set_topic(row[3])

        return connect_option
