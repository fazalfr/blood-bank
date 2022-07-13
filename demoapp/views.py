import datetime
from django.shortcuts import render
from .models import Users, Message



def home(request):
    return render(request,'home.html')
def register(request):
    return render(request,'register.html')
def success(request):
    username = request.POST['username']
    password = request.POST['password']
    number = request.POST['number']
    address = request.POST['address']
    group = request.POST['group']
    district = request.POST['district']
    age = request.POST['age']
    photo = request.FILES['photo']
    data = Users(username=username, password=password, number=number, address=address, district=district, age=age, photo=photo, group=group)
    data.save()
    return render(request, 'success.html')

def task(request):
    username2 = request.POST['l_username']
    password2 = request.POST['l_password']
    Users.objects.filter(username=username2, password=password2)
    if username2 == 'admin' and password2 == 'admin':
        return render(request, 'admin.html')
    elif Users.objects.filter(username=username2, password=password2):
        request.session['l_username'] = username2
        return render(request, 'index.html')
    else:
        return render(request, 'error.html')


def admin(request):
    return render(request,'admin.html')

def error(request):
    return render(request,'error.html')

def login(request):
    return render(request,'login.html')
def index(request):
    return render(request,'index.html')

def add(request):
    return render(request,'add.html')
def saved(request):
    name = request.POST['name']
    address = request.POST['address']
    group = request.POST['group']
    district = request.POST['district']
    age = request.POST['age']
    photo = request.FILES['photo']
    data = Users(name=name, address=address, district=district, age=age, photo=photo, group=group)
    data.save()
    return render(request, 'saved.html')

def show(request):
    data = Users.objects.all()
    return render(request, 'show.html', {'data': data})

def search(request):
    return render(request,'search.html')

def result(request):
    grp = request.GET['group']
    dis = request.GET['district']
    data = Users.objects.filter(group=grp, district=dis)
    return render(request, 'result.html', {'data': data})


def logout(request):
    try:
        del request.session['name']
    except:
        return render(request,'login.html')



def delete(request):
    return render(request,'delete.html')

def deleted(request):
    username = request.POST['username']
    data = Users.objects.get(username=username)
    data.delete()
    return render(request,'deleted.html')

def edit(request):
    return render(request,'edit.html')

def edited(request):
    username2 = request.session['l_username']
    group = request.POST['group']
    district = request.POST['district']
    age = request.POST['age']
    data = Users.objects.get(username=username2)
    data.group = group
    data.district = district
    data.age = age
    data.save()
    return render(request, 'edited.html', {'data': data})

def note(request):
    return render(request,'note.html')
def profile(request):
    name = request.session['l_username']
    data = Users.objects.filter(username=name)
    return render(request, 'profile.html', {'data': data})

def message(request):
    return render(request,'message.html')

def msges(request):
    group = request.POST['group']
    messages = request.POST['msg']
    date = request.POST['date']
    month = request.POST['month']
    year = request.POST['year']
    district = request.POST['district']
    hospital = request.POST['hospital']
    data = Message(group=group, message=messages, date=date, month=month, year=year, district=district, hospital=hospital)
    data.save()
    return render(request,'msges.html')

def notification(request):
    data = Message.objects.all()
    return render(request, 'notification.html', {'data': data})

def showmessage(request):
    data = Message.objects.all()
    return render(request, 'showmessage.html', {'data': data})

def dltmsg(request):
    msg = request.POST['msg']
    data = Message.objects.get(msg=msg)
    data.delete()
    return render(request,'dltmsg.html')
