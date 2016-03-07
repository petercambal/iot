from mysite.model.exception import PermissionException

class SecurityAdapter:

    cursor = None

    def __init__(self, cursor):
        self.cursor = cursor

    def __del__(self):
        pass


    def get_default_role_id(self):
        return "78c631a2-c54c-11e5-89ba-22000b79ceab"

    def check_permission(self, role_id, resource_method, resource_name):
        try:
            # retrieve resource id based on name and method
            query = "SELECT id from resource where name = '%s' and method = '%s'" % (resource_name,resource_method)

            self.cursor.execute(query)
            resource_id = self.cursor.fetchone()[0]

            if resource_id is None:
                raise ValueError("Resource not found")

            query = "SELECT count(*) from permission where role_id= '%s' and resource_id = '%s'" % (role_id,resource_id)
            self.cursor.execute(query)
            permission = self.cursor.fetchone()[0]

            if permission is 0:
                raise PermissionException("Access denied")

        except Exception as e:
            raise e