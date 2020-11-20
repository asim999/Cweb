
from datetime import datetime

from django.http import HttpResponse


class BaseMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

class ProcessExceptionMiddleware(BaseMiddleware):
    def process_exception(self, request, exception):
        print('----- Middleware view ')
        return HttpResponse("Exception Found")