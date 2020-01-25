from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api.serializers import HelloSerializer


class HelloApiView(APIView):
    '''Test API View'''

    serializer_class = HelloSerializer

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

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}, You have successfully done the post api call'
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        '''Handles updating an object'''
        return Response({
            'method': 'PUT'
        })

    def patch(self, request):
        '''Handles a partial update of an object'''
        return Response({
            'method': 'PATCH'
        })

    def delete(self, request):
        '''Delete an object'''
        return Response({
            'method': 'DELETE'
        })
