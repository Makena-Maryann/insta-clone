from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Profile,Comment
from .forms import NewPostForm,UpdateProfileForm,NewCommentForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.get_images()
    current_user = request.user
    return render(request, 'posts/index.html',{"posts":posts,"user":current_user})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    photos = Image.objects.filter(author=current_user).all()
    profile = Profile.objects.get(user=current_user)

    return render(request, 'posts/profile.html',{"photos":photos,"profile":profile})    

def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Image.search_by_caption(search_term)
        message = f"{search_term}"

        return render(request, 'posts/search.html',{"message":message,"posts":searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'posts/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
        comments = Comment.get_comments(image_id)
        number = len(comments)
        user = request.user
    except DoesNotExist:
        raise Http404()
    return render(request,"posts/image.html", {"image":image,"comments":comments,"number":number,"user":user})    

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = current_user
            post.save()
        return redirect('index')

    else:
        form = NewPostForm()
    return render(request,'new_post.html', {"form": form})                

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = UpdateProfileForm()
    return render(request,'update_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_comment(request,id):
    current_user = request.user
    image = Image.objects.filter(id = id)
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.image_id = id
            comment.save()
        return redirect('image')
    else:
        form = NewCommentForm()
        return render(request,'new_comment.html',{"form":form,"image":image})        
                                