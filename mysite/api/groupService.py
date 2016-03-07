from mysite.api.services.dbservice import DB

class GroupService:

    db = None
    cursor = None

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = self.db.cursor()
        print("GroupService - Opening")

    def __del__(self):
        if self.db:
            self.db.close()
            print("GroupService - Closing")

    def get(self, data):
        pass

    def post(self, data):
        pass