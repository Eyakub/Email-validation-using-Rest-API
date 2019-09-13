from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic.base import View
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import *


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class EmailApiView(APIView):
    serializer_class = EmailSerializer
    @csrf_exempt
    def get(self, request):
        return Response({'message': 'Test'})
    
    def post(self, request, format=None):
        params = json.loads(request.body)
        email = params.get('email')
        print(email)
        if email:
            if EmailValidation.objects.filter(email=email).exists():
                response ={
                    'message': 'Email already exists on Server'
                }
            else:
                e = EmailValidation()
                e.email = email
                e.save()
                response = {
                    'message': 'Email stored successful',
                    'status': True,
                }
            
        return Response(response)
    
