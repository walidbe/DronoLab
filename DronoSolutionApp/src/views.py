from .models import Image
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.

def home(request):

    if C.getCount(0) == -1:
        C.addCount(0)
        Arry.refresh(0)
        try:
            images = Image.objects.get(source="no-image.png")
        except Image.DoesNotExist:
            images = None

        return render(request, 'src/index.html', {'images': images,'images2':Arry.myObjects})

    else :
         images = Image.objects.order_by('created_date')[C.getCount(0)]
         if C.getCount(0) > 0 :

            for i in range(C.getCount(0)) :
                if i==3:
                  break
                nextElement = Arry.myObjects[i+1]
                Arry.myObjects[i+1] = Arry.myObjects[i]
                Arry.myObjects[i+2] = nextElement
            Arry.myObjects[0] = images
         else:
            Arry.myObjects[C.getCount(0)] = images

         C.addCount(0)
         return render(request, 'src/index.html', {'images': images,'images2':Arry.myObjects})

def post_pic(request):

        images = Image.objects.order_by('created_date')[C.getcount(0)]
        return render(request, 'src/index.html', {'images': images})



class C:
    count = -1   # number of times C.__init__ called

    def getCount(self):
        return C.count

    def addCount(self):
        C.count = C.count + 1

class Arry:
    myObjects =[]

    def refresh(self):
        for i in range(4) :
            Arry.myObjects.append(None)

