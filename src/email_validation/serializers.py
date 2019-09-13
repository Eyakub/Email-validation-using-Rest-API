from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import *

class EmailSerializer(serializers.Serializer):
    """serializersa name field for testing our EmailAPI"""
    name = serializers.CharField(validators=[UniqueValidator(queryset=EmailValidation.objects.all())])