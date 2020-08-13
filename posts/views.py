from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def index(request):
    posts = Image.get_images()
    return render(request, 'posts/index.html',{"posts":posts})

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Image.search_by_caption(search_term)
        message = f"{search_term}"

        return render(request, 'posts/search.html',{"message":message,"posts":searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'post/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"posts/image.html", {"image":image})    