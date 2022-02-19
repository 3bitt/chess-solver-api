from rest_framework.views import exception_handler
from solver.exceptions import DefaultServerErrorException_500


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
