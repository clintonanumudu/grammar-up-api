import os
import sys
from django.shortcuts import render
from django.http import HttpResponse
sys.path.append(os.path.dirname(__file__))
from generate import generateSentence

def sentence(request):
    return HttpResponse(generateSentence())