from django.shortcuts import render, redirect
from bookstore import models
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from bookstore import forms

# Create your views here.
@login_required
def index(request):
    all_tweets = models.Tweet.objects.all().order_by("-id")
    all_comments = models.Comment.objects.all()
    context = {'tweets':all_tweets, 'comments':all_comments}
    return render(request, "main.htm", context=context)

def delete_tweet(request):
    if request.method == "POST":
        print(request.POST)
        post_id = request.POST['id']
        models.Tweet.objects.get(id=post_id).delete()
        return HttpResponse("OK")

def edit_tweet(request):
    if request.method == "POST":
        post_id = request.POST['id']
        tweet = models.Tweet.objects.get(id=post_id)
        tweet.message = request.POST['description']
        tweet.save()

        return HttpResponse("Done")

@login_required
def add_comment(request):
    if request.method == "POST":
        tweet = models.Tweet.objects.get(id=request.POST['id'])
        models.Comment.objects.create(user=request.user, tweet=tweet, message=request.POST['comment'])
        return redirect("home")

@login_required
def add_tweet(request):
    if request.method == "POST":
        print(request.POST)
        models.Tweet.objects.create(user=request.user, message=request.POST['message'])
        return redirect("home")

def signup(request):
    if request.method == "POST":
        errors = []
        context = {}
        name = request.POST['name']
        lname = request.POST['lname']
        username = request.POST['username']
        userExists = User.objects.filter(username=username)
        if userExists:
            errors.append("نام کاربری انتخابی شما قبلا انتخاب شده است!")
            context['errors'] = errors
            return render(request, "signUp.htm", context=context)
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.first_name = name
        user.last_name = lname
        user.save()

        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect("home")
            # print("OK")

    return render(request, 'signUp.htm')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            print("FAILED! ")
    if request.user.is_authenticated:
        return redirect("home")

    return render(request, "signIn.htm")
