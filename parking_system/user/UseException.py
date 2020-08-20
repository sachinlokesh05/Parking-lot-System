from rest_framework.exceptions import APIException

class RoleNotExist(APIException):
    detail = "Mentioned Role is not present Under User"
    code = 404