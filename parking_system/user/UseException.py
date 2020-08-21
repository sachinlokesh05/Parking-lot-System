from rest_framework.exceptions import APIException

class RoleNotExist(APIException):
    detail = "Mentioned Role is not present Under User"
    code = 404

class LogOutFailed(APIException):
    detail = "Failed to SignOut,Please Try again later"