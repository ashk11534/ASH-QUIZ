
from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.home, name='home'),

    path('exams-on-category/<slug:category_slug>/', views.exams_on_category, name='exams-on-category'),

    path('exam-questions/<slug:exam_slug>/', views.exam_questions, name='exam-questions'),

    path('result/<exam_slug>/<marks>/<total_questions>/', views.result, name='result'),

    path('result-details/<exam_slug>/', views.result_details, name='result-details'),

]
