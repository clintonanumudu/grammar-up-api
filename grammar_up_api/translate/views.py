import os
import sys
from django.shortcuts import render
from django.http import HttpResponse
sys.path.append(os.path.dirname(__file__))
from translate_text import translateText

def translate(request):
    toTranslate = request.GET.get('text', 'Nothing to translate.')
    return HttpResponse(translateText(toTranslate))