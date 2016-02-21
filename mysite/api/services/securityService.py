from mysite.api.adapters.securityAdapter import SecurityAdapter

class SecurityService:

    db = None
    cursor = None

    # URL to resource conversion
    resources = [
            ("/api/proxy","proxy"),
            ("/api/entity", "virtualEntity")
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
        resource_name = None
        # search for resource by url
        for request_url , resource in self.resources:
            if request_url == request.path:
                resource_name = resource
                break

        # resource is not found in list
        if resource_name is None:
            raise ValueError("Resource not found")


        try:
            securityAdapter.check_permission(role_id, resource_method, resource_name)
        except Exception as e:
            raise e




