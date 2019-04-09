from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from suds.client import Client

WSDL_URL = 'http://localhost:8733/PostMeService/?singleWsdl'

# Create your views here.
def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'auth/login.html', c)

def do_login(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    client = Client(WSDL_URL)
    try:
        user = client.service.verify(username, password)
        request.session['isLoggedIn'] = True
        request.session['user'] = {
            'userId': user.userId,
            'username': user.username,
            'firstName': user.firstName,
            'lastName': user.lastName
        }
        print(user)
        return redirect('/')
    except:
        return redirect('/login')

def register(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'auth/register.html', c)

def do_register(request):
    try:
        client = Client("http://localhost:8733/PostMeService/?singleWsdl")
        u = client.factory.create('ns0:User')
        u.username = request.POST.get('username', '')
        u.firstName = request.POST.get('first_name', '')
        u.lastName = request.POST.get('last_name', '')
        u.password = request.POST.get('password', '')
        uid = client.service.addUser(u)
        print(uid)
        return redirect('/login')
    except:
        return redirect('/')

def logout(request):
    request.session['isLoggedIn'] = False
    return redirect('/')