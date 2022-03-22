from django.shortcuts import render,redirect
from django.http  import HttpResponse, Http404
from .forms import *
from .models import Image,Profile,Projects
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', locals())

@login_required(login_url='/accounts/login')
def welcome(request):
    current_user = request.user
    projects = Projects.objects.all()
    profile = Profile.objects.all()
    image = Image.objects.all()
    return render(request,'index.html', {'projects':projects,'profile':profile,'image':image,'current_user':current_user} )

@login_required(login_url='/accounts/login')
def search_results(request):
    if "image" in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm()
        projects = Projects.objects.filter(owner=current_user)
        profile = Profile.objects.get(user_id=current_user)
    return render(request, 'profile.html',{'profile':profile,'projects':projects,'current_user':current_user}, locals())


@login_required(login_url='/accounts/login')
def post_form(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = current_user
            image.save()
            return redirect('/')
    else:
        form = UploadForm()
    return render(request, 'post.html', {'form': form})

def login(request):
    return render(request, 'registration/login.html')

@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    return logout