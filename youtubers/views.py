from django.shortcuts import render
from .models import Youtuber
# Create your views here.
def youtubers(request):
    tubers=Youtuber.objects.order_by('-created_date')
    data={
      'tubers':tubers,
    }
    return render(request,'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    return render(request,'youtubers/youtubers_details.html')

def search(request):
    pass
