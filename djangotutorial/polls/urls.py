from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('<int:question_id>/detail/', views.detail, name = 'Detail'),
    path('<int:question_id>/result/', views.results, name = 'Result'),
    path('<int:question_id>/vote/', views.vote, name = "Vote"),
    
]