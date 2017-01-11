# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import pdfParse
filepath = '/home/phoenx/geo.pdf'

def index(request):
    return render(request, 'schedulr/index.html')

def pdfone(request):
    pdfparse = pdfParse()
    toPrint_list = pdfparse.__str__()
    return HttpResponse(toPrint_list)

def pdftwo(request):
    pdfparse = pdfParse()
    toPrint_list = pdfparse.__str__()
    return HttpResponse(toPrint_list)
