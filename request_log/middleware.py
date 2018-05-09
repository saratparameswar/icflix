from models import LogApi
from questions.models import Tenant


class RequestLogMiddleware(object):

    def process_response(self, request, response):


        log_data = {
            'user': request.user.pk,
            'request_method': request.method,
            'request_path': request.get_full_path(),
            'request_body': request.body,
            'response_status': response.status_code,

        }

        # save log_data
        if not request.user.is_anonymous:
            try:
                tenant_obj = Tenant.objects.get(user=request.user)
                LogApi.objects.create(tenant=tenant_obj, data=log_data)
            except Tenant.DoesNotExist:
                pass
        return response