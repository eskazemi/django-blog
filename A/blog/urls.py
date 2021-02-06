from django.urls import path
from .import views

app_name='blog'

urlpatterns=[
    path('all_articles/',views.all_articles,name='all_articles'),
    path('all_articles/<int:id>/<slug:slug>/',views.article_detail,name='article_detail'),
]