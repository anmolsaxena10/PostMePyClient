from django.shortcuts import render, redirect
from suds.client import Client
import json

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
