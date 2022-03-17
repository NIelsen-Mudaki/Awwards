from django.shortcuts import render
from . import views
from .models import Image, Profile, Ratings

# Create your views here.
def home(request):
    context = {
        'images':Image.objects.all()
    }
    return render(request, ('wowawards/profile.html'), context)