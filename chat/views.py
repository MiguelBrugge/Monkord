from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Profile, Chat, Message
from django.utils import timezone

# Authentication
def user_login(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            userList = User.objects.exclude(username=user.username)
            return redirect("/home?userId=" + str(userList.first().pk))
        
    logout(request)
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

# Main Views
@login_required(login_url='/')
def home(request):
    user = request.user
    profile = get_profile(user)

    userList = User.objects.exclude(username=user.username)
    profiles = Profile.objects.filter(user__in=userList).exclude(user=user)
    
    user_profile_list = sorted(zip(userList, profiles), key=lambda x: x[0].pk)
    chat = None
    otherChatMember = None

    if request.GET.get("userId"):
        otherUser = User.objects.get(id=request.GET.get("userId"))
        otherProfile = Profile.objects.get(user=otherUser)
        chat = Chat.objects.filter(members=profile).filter(members=otherProfile).first()
        
        if chat is None:
            chat = Chat.objects.create()
            chat.members.set([profile, otherProfile])
            chat.save()
        otherChatMember = {"user": otherUser, "profile": otherProfile}

    try:
        messages = Message.objects.filter(chat=chat)
    except Message.DoesNotExist:
        messages = None

    context = {
        "user": user,
        "profile": profile,
        "user_profile_list": user_profile_list,
        "chat": chat,
        "messages": messages,
        "otherChatMember": otherChatMember,
    }
    return render(request, "home.html", context)

@login_required(login_url='/')
def update_profile_status(request):
    user = request.user
    profile = get_profile(user)
    profile.status = request.POST.get('status')
    profile.save()
    link = request.POST.get('link')
    return redirect(link)

# Methods
def get_profile(user):
    return Profile.objects.get(user=user)