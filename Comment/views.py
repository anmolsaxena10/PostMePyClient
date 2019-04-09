from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from suds.client import Client
from datetime import datetime

# Create your views here.
def add_comment(request):
    c = {}
    c.update(csrf(request))
    c['postId'] = request.GET.get('postId', '')
    c['replyOfComment'] = request.GET.get('replyOfComment', '')
    if c['postId'] == '':
        return redirect('/')
    return render(request, 'comment/add.html', c)

def do_add_comment(request):
    try:
        client = Client("http://localhost:8733/PostMeService/?singleWsdl")
        c = client.factory.create('ns0:Comment')
        c['time'] = datetime.now()
        c['description'] = request.POST.get('description', '')
        c['upvotes'] = 0
        c['replyOfComment'] = int(request.POST.get('replyOfComment', -1))
        c['user'] = client.factory.create('ns0:User')
        c['user'].userId = request.session['user']['userId']
        c['post'] = client.factory.create('ns0:Post')
        c['post'].postId = int(request.POST.get('postId', 2))
        print("asd")
        commentId = client.service.addComment(c)
        print(commentId, c['replyOfComment'])
        return redirect('/ViewPost?id=' + request.POST.get('postId', 2))
    except:
        return redirect('/ViewPost?id=' + request.POST.get('postId', 2))

def delete_comment(request):
    pass