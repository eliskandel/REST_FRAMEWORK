from django.urls import path
from .views import (BlogViewList,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView,
                    BlogRetrieveView,
                    CommentViewList,
                    CommentCreateView,
                    CommentUpdateView,
                    CommentDeleteView,
                    CommentRetrieveView)
urlpatterns=[
    path("",BlogViewList.as_view()),
    path("create/",BlogCreateView.as_view()),
    path("update/<int:pk>/",BlogUpdateView.as_view()),
    path("delete/<int:pk>/",BlogDeleteView.as_view()),
    path("read/<int:pk>/",BlogRetrieveView.as_view()),
    path("comment/",CommentViewList.as_view()),
    path("create/",CommentCreateView.as_view()),
    path("update/<int:pk>/",CommentUpdateView.as_view()),
    path("delete/<int:pk>/",CommentDeleteView.as_view()),
    path("read/<int:pk>/",CommentRetrieveView.as_view()),
]