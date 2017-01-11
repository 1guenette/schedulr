from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /schedulr/
    url(r'^$', views.index, name='index'),
    url(r'^pdfone/$', views.pdfone, name='pdfone'),
    url(r'^pdftwo/$', views.pdftwo, name='pdftwo'),
]
