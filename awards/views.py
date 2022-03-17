from django.shortcuts import render
from django.http  import HttpResponse
from . import views
from .models import Image,Profile

# Create your views here.
def welcome(request):
    
    return render(request,'index.html')

def search_results(request):
    if "image" in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})