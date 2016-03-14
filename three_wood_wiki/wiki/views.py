from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from wiki.models import UserProfile


def home(request):
    return HttpResponseRedirect('/index')


@login_required(login_url='../login')
def index(request):
    t = get_template('index.html')
    userProfile = UserProfile.objects.get(user=request.user)
    html = t.render({"name": userProfile.name, "phone_num": userProfile.phone_num})
    return HttpResponse(html)


def login_page(request):
    t = get_template('login.html')
    html = t.render({})
    return HttpResponse(html)


def register_page(request):
    t = get_template('register.html')
    html = t.render({})
    return HttpResponse(html)


@csrf_exempt
def check_login(request):
    username = str(request.POST['username'])
    password = str(request.POST['password'])
    remember = request.POST['remember']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            print(remember)
            if remember == "true":
                request.session.set_expiry(10000)
            else:
                request.session.set_expiry(0)
            result_dict = {'result':True}
            return JsonResponse(result_dict)

    result_dict = {'result':False}
    return JsonResponse(result_dict)


@csrf_exempt
def check_username(request):
    username = str(request.POST['username'])
    if username == '':
        return JsonResponse({"check": False})
    user = User.objects.filter(username=username)
    if len(user):
        return JsonResponse({"check": False})
    return JsonResponse({"check": True})


@csrf_exempt
def register_user(request):
    username = str(request.POST['username'])
    password = str(request.POST['password'])
    phone_num = str(request.POST['phone_num'])
    email = str(request.POST['email'])
    name = str(request.POST['name'])
    if username=='' or password=='' or phone_num=='' or email=='' or name=='':
        return JsonResponse({'result': False})
    user = User.objects.filter(username=username)
    if len(password)>5 and len(password)<13 and not len(user):
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        userProfile = UserProfile.objects.create(user=user, phone_num=phone_num, name=name)
        userProfile.save()
        result_dict = {'result':True}
        return JsonResponse(result_dict)
    result_dict = {'result': False}
    return JsonResponse(result_dict)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('../login')