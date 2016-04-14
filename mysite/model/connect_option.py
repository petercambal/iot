class ConnectOption:
    def __init__(self):
        self.id = None
        self.protocol = None
        self.topic = None

    def get_id(self):
        return self.id

    def get_protocol(self):
        return self.protocol

    def get_topic(self):
        return self.topic

    def set_id(self, id):
        self.id = id

    def set_protocol(self, protocol):
        self.protocol = protocol

    def set_topic(self, topic):
        self.topic = topic

    def toJSON(self):

        return {
            "id": self.id,
            "protocol": self.protocol,
            "topic": self.topic
        }

    @staticmethod
    def fromJSON(json_data):
        if json_data is not None:
            if not isinstance(json_data, dict):
                raise ValueError("Parameter data must be instance of dictionary %s found" % type(json_data))

            connect_option = ConnectOption()
            connect_option.set_id(json_data.get('id'))
            connect_option.set_protocol(json_data.get('protocol'))
            connect_option.set_topic(json_data.get('topic'))

            return connect_option

        return None
