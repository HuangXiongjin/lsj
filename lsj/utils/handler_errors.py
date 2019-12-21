from rest_framework.exceptions import APIException


class ParamsException(APIException):
    def __init__(self, detail):
        self.detail = detail
