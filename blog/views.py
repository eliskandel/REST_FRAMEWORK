from django.shortcuts import render
from .models import Blog,Comment
from .serializers import BlogSerializer,CommentSerializer
# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)

class BlogViewList(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
class BlogCreateView(CreateAPIView):
    serializer_class=BlogSerializer
    
class BlogUpdateView(UpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    
class BlogDeleteView(DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    

class BlogRetrieveView(RetrieveAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
     # fsajdaskd    # fsajdaskd   
class CommentViewList(ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
class CommentCreateView(CreateAPIView):
    serializer_class=CommentSerializer
    
class CommentUpdateView(UpdateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    
class CommentDeleteView(DestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
class CommentRetrieveView(RetrieveAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer