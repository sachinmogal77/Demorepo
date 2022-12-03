import imp
from django.urls import path
from . import views

urlpatterns = [
    path('stu/',views.StudentApi.as_view()),
    path('stu/<int:pk>/',views.StudentDetailsApi.as_view())
]