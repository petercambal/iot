from mysite.api.adapters.securityAdapter import SecurityAdapter
from mysite.api.services.dbservice import DB

class SecurityService:

    db = None
    cursor = None

    # URL to resource name conversion
    resources = [
            ("/api/proxy","proxy"),
            ("/api/device", "device"),
            ("/api/entity", "virtualEntity"),
            ("/api/property", "property"),
            ("/api/domain", "domain"),
            ("/api/group", "group"),
            ("/login" , "login"),
            ("/logout", "logout"),
            ("/register", "register"),
            ("/", "root")
        ]

    def __init__(self):
        db = DB().connect()
        self.db = db
        self.cursor = self.db.cursor()

    def __del__(self):
        if self.db:
            self.db.close()

    def check_access_permission(self,request):
        securityAdapter = SecurityAdapter(self.cursor)
        session = request.session
        try:
            user = session['user']
            role_id = user.get_role().get_id()
        except Exception:
            role_id = securityAdapter.get_default_role_id()

        resource_method = request.method

        # apply rbac only on /api requests
        if not request.path.startswith('/api'):
            return

        if resource_method == "POST":
            resource_method = "SET"

        resource_name = None
        # search for resource by url
        for request_url , resource in self.resources:
            if request.path.startswith(request_url):
                resource_name = resource
                break
        # resource is not found in list
        if resource_name is None:
            raise ValueError("Resource not found")

        try:
            securityAdapter.check_permission(role_id, resource_method, resource_name)
        except Exception as e:
            raise e




