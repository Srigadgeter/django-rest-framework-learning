from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    "Serializes a name field for testing a HelloApiView"
    name = serializers.CharField(max_length=10)
