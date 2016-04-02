from mysite.model.log import Log

class LogAdapter:
    cursor = None

    def __init__(self, cursor):
        self.cursor = cursor

    def __del__(self):
        pass

    def insert(self, log):
        query = "INSERT INTO `log` (id,resource_id,role_id,info,timestamp) VALUES ('%s','%s','%s','%s', CURRENT_TIMESTAMP())" % (

            log.get_id(),
            log.get_resource_id(),
            log.get_role_id(),
            log.get_info()
        )
        try:
            self.cursor.execute(query)
        except Exception as e:
            raise e

    def get_all(self):
        query = "SELECT * FORM log"

        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        logs = []
        for row in rows:
            log = self.create(row)
            logs.append(log)

    def create(self, row):

        log = Log()
        log.set_id(row[0])
        log.set_resource_id(row[1])
        log.set_role_id(row[2])
        log.set_info(row[3])
        log.set_timestamp(row[4])

        return log
