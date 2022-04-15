from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def login_page(request):

    context = {"title": "Neighborhood - Login"}
    return render(request, 'hood/login.html', context)


def register_page(request):

    context = {"title": "Neighborhood - Sign Up"}
    return render(request, 'hood/register.html', context)


# @login_required(login_url='/login')
def neighborhoods_page(request):

    context = {"title": "Neighborhood - Hoods"}
    return render(request, 'hood/neighborhoods.html', context)


# @login_required(login_url='/login')
def create_profile_page(request):

    context = {"title": "Neighborhood - Create Profile"}
    return render(request, 'hood/create_profile.html', context)


# @login_required(login_url='/login')
def index(request):

    context = {"title": "Neighborhood - Home"}
    return render(request, 'hood/index.html', context)
