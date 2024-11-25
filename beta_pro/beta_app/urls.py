from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('contact',views.contact),
    path('about',views.about),
    path('course_dtl/<c_id>',views.courses_dtl),
    path('view_course',views.view_course),
]