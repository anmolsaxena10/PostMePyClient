from django.shortcuts import render
from suds.client import Client

def home(request):
    currPage = request.GET.get('page', 1)
    currPage = int(currPage)
    prevPage = 1 if currPage == 1 else currPage - 1
    client = Client("http://localhost:8733/PostMeService/?singleWsdl")
    posts = client.service.filterPosts(currPage, None, None, None)[0]
    nextPage = currPage if len(posts) < 10 else currPage + 1
    c = {
        'currPage' : currPage,
        'nextPage' : nextPage,
        'prevPage' : prevPage,
        'posts' : posts
    }
    return render(request, 'home/index.html', c)