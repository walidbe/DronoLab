from .models import Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.

cnt =0
def home(request):

        images = Image.objects.order_by('created_date')[0]
        return render(request, 'src/index.html', {'images': images})

def post_pic(request):

        images = Image.objects.order_by('created_date')[cnt+1]
        return render(request, 'src/index.html', {'images': images})
