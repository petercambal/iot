import MySQLdb

class DB:

    @staticmethod
    def connect():
        conn =MySQLdb.connect(
        host='iot.mysql.pythonanywhere-services.com',
        user='iot',
        passwd='ChallengerSRT8',
        db='iot$database')

        conn.autocommit(False)

        return conn