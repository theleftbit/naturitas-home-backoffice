from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView


class HealthCheck(APIView):
    """
    Check server availability
    """

    def get(self, *args, **kwargs):
        return Response({'success': True, 'msg': u'Server is alive'}, status=HTTP_200_OK)
