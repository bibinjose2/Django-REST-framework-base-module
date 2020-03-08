from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR


class HttpSuccessResponse(Response):
    def __init__(self, data=None, message=None, status=None, **kwargs):
        data = {
            'status': status if status else HTTP_200_OK,
            'message': message if message else '',
            'data': data if data else []
        }
        self.status_code = status if status else HTTP_200_OK
        super(HttpSuccessResponse, self).__init__(data, **kwargs)


class HttpErrorResponse(Response):
    def __init__(self, message, status=None, **kwargs):
        data = {
            'status': status if status else HTTP_500_INTERNAL_SERVER_ERROR,
            'message': message
        }
        self.status_code = status if status else HTTP_500_INTERNAL_SERVER_ERROR
        super(HttpErrorResponse, self).__init__(data, **kwargs)
