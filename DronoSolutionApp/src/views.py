from django.shortcuts import render
import os.path
from django.http import HttpResponse

# Create your views here.


def home(request):

    return render(request, 'src/index.html', {});
