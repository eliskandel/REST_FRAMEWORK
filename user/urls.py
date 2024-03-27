from django.urls import path
from .views import UserViewList,UserCreateView
urlpatterns=[
    path("",UserViewList.as_view()),
    path("create/",UserCreateView.as_view())
]