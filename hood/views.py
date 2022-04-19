from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect


# Create your views here.
from hood.forms import PostForm
from hood.models import Profile, Neighborhood, Member, Post, Business


def login_page(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        # Getting the user's info
        username = request.POST.get('identifier_field')
        password = request.POST.get('password_field')
        # Checking if the user exists
        try:
            # The authenticate fun below will either return a user obj. tha matches the cred.s we've provides or None
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # The login fun will add a session for the user logging them in
                login(request, user)

                # Once the user has been logged in successfully we wanna redirect them to the home page
                return redirect('/create-profile')
            else:
                messages.error(request, "The username and password don't matches")

        except :
            messages.error(request, "The username and password don't match")

    context = {"title": "Neighborhood - Login"}
    return render(request, 'hood/login.html', context)


def register_page(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        # Getting the user's info
        username = request.POST.get('username_field')
        name = request.POST.get('name_field')
        email = request.POST.get('email_field')
        password = request.POST.get('password_field')
        # Checking if the user exists
        try:
            user = User.objects.get(username=username)

            if user is None:
                new_user = User.objects.create_user(first_name=name, username=username, email=email, password=password)

                Profile.objects.create(user=new_user, bio='', neighborhood_name='empty', neighborhood=None,
                                       gen_location='empty')
                # Once the user has been logged in successfully we wanna redirect them to the home page
                print("The creation was successful")
                return redirect('/login')
            else:
                print("The creation was not successful")

        except :
            new_user = User.objects.create_user(username=username, first_name=name, email=email, password=password)

            Profile.objects.create(user=new_user, bio='', neighborhood_name='empty', neighborhood=None,
                                   gen_location='empty')
            # Once the user has been logged in successfully we wanna redirect them to the home page
            print("The creation was successful")
            return redirect('/login')
            # messages.error(request, "The username and password don't match")

    context = {"title": "Neighborhood - Sign Up"}
    return render(request, 'hood/register.html', context)


@login_required(login_url='/login')
def neighborhoods_page(request):
    neighborhoods = Neighborhood.objects.all()
    context = {"title": "Neighborhood - Hoods", "neighborhoods": neighborhoods}
    return render(request, 'hood/neighborhoods.html', context)


@login_required(login_url='/login')
def selected_neighborhood_page(request, n_id):
    neighborhood = Neighborhood.objects.filter(id=n_id).first()
    if neighborhood:
        # Incr the members count by one
        neighborhood.members_count = neighborhood.members_count + 1
        neighborhood.save()
        # Get the profile and update the neighborhood
        user_profile = Profile.objects.filter(user__id=request.user.id).first()
        if user_profile:
            # update the user's neighborhood
            user_profile.neighborhood = neighborhood
            user_profile.save()
        # Add an else so that we can cancel the execution
        else:
            return redirect('/neighborhoods')
        # get the user's member item and update it else create it
        user_member = Member.objects.filter(user__id=request.user.id).first()
        if user_member:
            user_member.status = 0
            user_member.neighborhood = neighborhood
            user_member.save()
        else:
            # we're gonna create the member
            Member.objects.create(user=request.user, status=0, neighborhood=neighborhood)
        return redirect('/')
    else:
        return redirect('/neighborhoods')


@login_required(login_url='/login')
def create_profile_page(request):
    profile = Profile.objects.filter(user__id=request.user.id).first()
    # user_member = Member.objects.filter(user__id=request.user.id).first()

    if profile and profile.phone != 'empty':
        return redirect('/')

    if request.method == "POST":
        neighborhood_name = request.POST.get('neighborhood_name_field')
        phone = request.POST.get('phone_field')
        location = request.POST.get('gen_loc_field')
        bio = request.POST.get('bio_field')

        profile.neighborhood_name = neighborhood_name
        profile.bio = bio
        profile.phone = phone
        profile.gen_location = location
        profile.save()
        return redirect('/')

    context = {"title": "Neighborhood - Create Profile", 'profile': profile}
    return render(request, 'hood/create_profile.html', context)


@login_required(login_url='/login')
def search_page(request):
    search_req = request.GET.get('q') if request.GET.get('q') is not None else ''

    results = Business.objects.filter(
        Q(name__icontains=search_req) |
        Q(location__icontains=search_req) |
        Q(email__icontains=search_req)
    ).all()
    results_count = len(results)

    context = {'title': f'Search - {search_req}', 'results': results, 'results_count': results_count,
               'search_str': search_req}

    return render(request, 'hood/search.html', context)


@login_required(login_url='/login')
def index(request):
    # user_profile = Profile.objects.filter(user__id=request.user.id).first()

    user_member = Member.objects.filter(user__id=request.user.id).first()
    # check if the user has a neighborhood selected
    if user_member and user_member.neighborhood:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            form.instance.user = request.user
            form.instance.neighborhood = user_member.neighborhood
            if form.is_valid():
                form.save()
                return redirect('/')
        form = PostForm()
        posts = Post.objects.filter(neighborhood=user_member.neighborhood).all()
        context = {"title": f"Neighborhood - {user_member.neighborhood.name}", 'status': user_member.status,
                   'form': form, 'posts': posts, 'user_member': user_member}
        return render(request, 'hood/index.html', context)
    else:
        return redirect('/neighborhoods')


@login_required(login_url='/login')
def leave_community_page(request):
    user_member = Member.objects.filter(user__id=request.user.id).first()
    print(f'The member {user_member}')
    if user_member:
        neighborhood = user_member.neighborhood
        neighborhood.members_count = neighborhood.members_count - 1
        neighborhood.save()

        user_member.neighborhood = None
        user_member.status = 0
        user_member.save()
        return redirect('/neighborhoods')
    else:
        return redirect('/')

