from rest_framework.exceptions import APIException
from rest_framework import status


class ConflictException_409(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Field does not exist."
    default_code = "field_does_not_exist"


class NotFoundException_404(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Figure not found."
    default_code = "figure_not_found"


class DefaultServerErrorException_500(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = "unknown_error"
