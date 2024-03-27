from django.shortcuts import render
from .models import User
from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView

# Create your views here.
# class UserViewList(APIView):
#     def get(self,request,*args,**kwargs):
#         users=User.objects.all()
#         serializer=UserSerializer(users,many=True)
        
#         return Response(serializer.data)
    
# class UserCreateView(APIView):
#     def post(self,*args,**kwargs):
#         serializer=UserSerializer(data=self.request.data)
#         serializer.is_valid(raise_exception=True)
#         user_name=serializer.validated_data.get("user_name")
#         first_name=serializer.validated_data.get("first_name")
#         last_name=serializer.validated_data.get("last_name")
#         age=serializer.validated_data.get("age")
#         User.objects.create(user_name=user_name,first_name=first_name,last_name=last_name,age=age)
#         return Response({"message":"User created"})

class UserViewList(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
class UserCreateView(CreateAPIView):
    serializer_class=UserSerializer