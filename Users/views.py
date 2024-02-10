from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework import status
from .models import CustomUser

@api_view(['GET'])
def hello_world(request):
    return Response({'status':200, 'message':"Hello World"})

@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_user_by_id(request,user_id):
    obj_ = CustomUser.objects.get(pk=user_id)
    serializer = UserSerializer(obj_)
    return Response(serializer.data)

@api_view(["GET"])
def get_user_details(request):
    user = CustomUser.objects.all()
    serializer = UserSerializer(user, many=True)

    return Response(serializer.data)





