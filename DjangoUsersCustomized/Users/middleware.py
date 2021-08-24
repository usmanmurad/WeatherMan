# custom middleware for restricting access on IP basis


from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

ALLOWED_IPS = ['129.0.0.1', '127.0.0.1']


class IpCheckMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("in custom middleware")
        ip = request.META['REMOTE_ADDR']
        print(ip)
        if ip in ALLOWED_IPS:
            print("in if")
            return None
        else:
            print("in else")
            return HttpResponseForbidden()
