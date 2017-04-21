from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^glossary/', views.glossary, name='glossary'), 
    url(r'^about/', views.about, name='about')
]
