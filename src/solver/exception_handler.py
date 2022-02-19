from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        message = response.data.get("detail")
        if not message:
            raise DefaultServerErrorException_500("Internal Server Error")
        else:
            response.data = {
                "error": str(message),
            }

    return response


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
