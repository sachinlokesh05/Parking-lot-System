from rest_framework.exceptions import APIException

class RoleNotExist(APIException):
    default_detail = "Mentioned Role is not present Under User"
    status_code = 404

class LogOutFailed(APIException):
    status_code = "Failed to SignOut,Please Try again later"


class SomeOneIsLoggedInAlready(APIException):
    default_detail="Already Someone is logged in,Please Logout and Try Login"
    status_code = 400