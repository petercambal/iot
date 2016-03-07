from mysite.api.adapters.userAdapter import UserAdapter
from mysite.api.services.dbservice import DB

class UserService:

    db = None
    cursor = None

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = self.db.cursor()

    def __del__(self):
        if self.db:
            self.db.close()

    def get_user(self,request):
        try:
            session = request.session
            if session['user']:
                return session['user']
            else:
                return None
        except:
            return None


    def sign_out(self,request):

        try:
            session = request.session
            if session['user']:
                session.delete()
        except Exception as e:
            raise e

    def sign_in(self,request):
        userAdapter = UserAdapter(self.cursor)
        session = request.session

        try:
            user = userAdapter.sign_in(request.json)
            session['user'] = user
        except Exception as e:
            raise e

    def register(self,user_data):
        user_data.update({"role" : "78c631a2-c54c-11e5-89ba-22000b79ceab"})
        userAdapter = UserAdapter(self.cursor)

        try:

            userAdapter.register(user_data)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def post(self,data):
        pass

    def delete(self,data):
        pass