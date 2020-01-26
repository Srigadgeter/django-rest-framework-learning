from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.authentication import TokenAuthentication

from .serializers import HelloSerializer, UserProfileSerializer
from .models import UserProfile
from .permissions import UpdateOwnProfile


class HelloApiView(APIView):
    '''Test API View'''

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        data = [
            'Django Rest Framework',
            'APIView Example',
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

    def put(self, request, pk=None):
        '''Handles updating an object'''
        return Response({
            'method': 'PUT'
        })

    def patch(self, request, pk=None):
        '''Handles a partial update of an object'''
        return Response({
            'method': 'PATCH'
        })

    def delete(self, request, pk=None):
        '''Delete an object'''
        return Response({
            'method': 'DELETE'
        })


class HelloViewSet(ViewSet):
    '''Test API ViewSet'''

    serializer_class = HelloSerializer

    def list(self, request):
        data = [
            'Django Rest Framework',
            'ViewSet Example',
            'Test API Call'
        ]
        return Response({
            'message': 'Hello, I\'m the first ViewSet API call',
            'data': data
        })

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({
                'message': message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''Handles getting an object'''
        return Response({
            'http_method': 'GET'
        })

    def update(self, request, pk=None):
        '''Handles update of an object'''
        return Response({
            'http_method': 'PUT'
        })
    
    def partial_update(self, request, pk=None):
        '''Handles partial update of an object'''
        return Response({
            'http_method': 'PATCH'
        })
    
    def destroy(self, request, pk=None):
        '''Handles removing/deleting an object'''
        return Response({
            'http_method': 'DELETE'
        })
    

class UserProfileViewSet(ModelViewSet):
    '''ViewSet for an UserProfile Model'''

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)

