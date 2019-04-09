from django.shortcuts import render, redirect
from suds.client import Client
import json
from django.template.context_processors import csrf
from datetime import datetime

# Create your views here.
def view_post(request):
    postId = request.GET.get('id', '')
    if(postId == ''):
        return redirect('/')
    client = Client("http://localhost:8733/PostMeService/?singleWsdl")
    comments = client.service.filterComments(None, postId, None)
    try:
        comments = comments[0]
    except:
        comments = None
    c = {
        'post': client.service.getPost(int(postId)),
        'comments': comments
    }
    return render(request, 'view_post.html', c)

def add_post(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'post/add.html', c)

def do_add_post(request):
    try:
        client = Client("http://localhost:8733/PostMeService/?singleWsdl")
        p = client.factory.create('ns0:Post')
        p.description = request.POST.get('description', '')
        p.headline = request.POST.get('headline', '')
        p.time = datetime.now()
        p.upvotes = 0
        p.user = client.factory.create('ns0:User')
        p.user.userId = request.session['user']['userId']
        print(p)
        pid = client.service.addPost(p)
        print(pid)
        return redirect('ViewPost?id=' + str(pid))
    except:
        return redirect('/')