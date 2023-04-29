from django.shortcuts import render
from django.http import HttpRequest
from . models import Data
# Create your views here.
def testPage(request):
    
    if 'q' in request.GET :
        q = request.GET['q']
      
        data = Data.objects.filter(first_name__icontains=q)
        
        
    else:
        data = Data.objects.all() 
        print('test2')
    names = {
        'data' : data
    }

    return render(request, 'tes.html', names)
