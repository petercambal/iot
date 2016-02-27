from mysite.api.adapters.securityAdapter import SecurityAdapter

class SecurityService:

    db = None
    cursor = None

    # URL to resource name conversion
    resources = [
            ("/api/proxy","proxy"),
            ("/api/device", "device"),
            ("/api/entity", "virtualEntity"),
            ("/api/property", "property"),
            ("/api/group", "group"),
            ("/login" , "login"),
            ("/logout", "logout"),
            ("/register", "register"),
            ("/", "root")
        ]

    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()

    def check_access_permission(self,request):
        securityAdapter = SecurityAdapter(self.cursor)
        session = request.session
        try:
            user = session['user']
            role_id = user.get_role().get_id()
        except Exception:
            role_id = securityAdapter.get_default_role_id()

        resource_method = request.method

        # exclude public, admin and static requests from rbac
        if request.path.startswith('/public') or request.path.startswith('/admin') \
        or request.path.startswith('/static') or request.path.startswith('/fonts'):
            return

        if resource_method == "POST":
            resource_method = "SET"


        resource_name = None
        # search for resource by url
        for request_url , resource in self.resources:
            if request_url == request.path:
                resource_name = resource
                break

        # resource is not found in list
        if resource_name is None:
            raise ValueError("Resource not found")

        # exclude public functions from rbac
        if resource_name in ["login","logout","register","root"]:
            return

        try:
            securityAdapter.check_permission(role_id, resource_method, resource_name)
        except Exception as e:
            raise e




