from mysite.api.adapters.userAdapter import UserAdapter

class UserService:

    db = None
    cursor = None

    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()

    def get(self,data):
        pass

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