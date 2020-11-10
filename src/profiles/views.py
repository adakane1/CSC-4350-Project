from django.shortcuts import render

from .forms import ProfileUpdateForm
from .models import Profile

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

def profile_fill_view(request):
    instance = Profile.objects.get(user=request.user)
    form = ProfileUpdateForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('dash')
    context = {
        'form': form
    }
    return render(request, "profiles/profile_fill.html", context)

def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        # profile_form = ProfileForm(request.POST or None)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            print(request.user)
            # print(request.user_id)

            # if profile_form.is_valid():
            #     profile_form.save()
            return redirect('profilefill')
    else:
        user_form = UserCreationForm()
    # return render(request, 'profiles/signup.html', {'u_form': user_form, 'p_form': profile_form})
    return render(request, 'profiles/signup.html', {'u_form': user_form})

# def user_detail_view(request):
#     obj = Profile.objects.get(id=1)

#     context = {
#         'object': obj
#     }
#     return render(request, "profiles/detail.html", context)

def user_create_view(request, *args, **kwargs):
    return render(request, "profiles/user_create.html", {})

def user_detail_view(request, *args, **kwargs):
    obj = Profile.objects.get(user=request.user)
    context = {
        'object' : obj
    }
    print(obj.age)
    return render(request, "profiles/detail.html", {})

