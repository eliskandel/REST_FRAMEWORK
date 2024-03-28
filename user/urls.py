from django.urls import path
from .views import UserViewList,UserCreateView,UserUpdateView,UserDeleteView,UserRetrieveView
urlpatterns=[
    path("",UserViewList.as_view()),
    path("create/",UserCreateView.as_view()),
    path("update/<int:pk>/",UserUpdateView.as_view()),
    path("delete/<int:pk>/",UserDeleteView.as_view()),
    path("read/<int:pk>/",UserRetrieveView.as_view()),
    
]