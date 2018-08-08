from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'CourseList/', views.CourseList.as_view()),
    url(r'CourseDetail/', views.CourseDetail.as_view())
]
