from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Secret
from django.db.models import Count

def index(request):
    return render(request, 'secrets/index.html')

def registration(request):
    validationCheck = User.usermanager.register(request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
    if 'theUser' in validationCheck:
        if not 'user' in request.session:
            request.session['user'] = validationCheck['theUser'].id
        return redirect('/secrets')
    elif 'errors' in validationCheck:
        for message in validationCheck['errors']:
            messages.error(request, message)
        return redirect('/')

def login(request):
    loginCheck = User.usermanager.login(request.POST['email'], request.POST['password'])
    if 'theUser' in loginCheck:
        if not 'user' in request.session:
            request.session['user'] = loginCheck['theUser'].id
        return redirect ('/secrets')
    if 'errors' in loginCheck:
        for message in loginCheck['errors']:
            messages.error(request, message)
        return redirect('/')

def logout(request):
    request.session.pop('user')
    messages.success(request, 'You have logged out')
    return redirect('/')

def secrets(request):
    context ={
        'users': User.usermanager.get(id=request.session['user']),
        'secrets': Secret.objects.all(),
    }
    return render(request, 'secrets/secret.html', context)

def secret_post(request):
    user= User.usermanager.get(id=request.session['user'])
    Secret.objects.create(secret=request.POST['secret'], user=user)
    return redirect('/secrets')

def delete(request, id):
    Secret.objects.filter(id=id).delete()
    return redirect ('/secrets')

def like(request, id):
    this_user= User.usermanager.get(id=request.session['user'])
    this_secret= Secret.objects.get(id=id)
    this_secret.likes.add(this_user)
    return redirect ('/secrets')

def popular(request):
    context={
        'secrets': Secret.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
    }
    return render (request, 'secrets/popular.html', context)
