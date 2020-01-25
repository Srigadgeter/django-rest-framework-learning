from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        data = [
            'Django Rest Framework',
            'API Example',
            'Test GET API Call'
        ]

        return Response({
            'message': 'This is GET api call',
            'data': data
        })
