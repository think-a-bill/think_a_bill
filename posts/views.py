from django.shortcuts import render, redirect
from .forms import PostForm

# Create your views here.
def index_redirect(request):
    return redirect('reviews:index')

def index(request):
    context = {
        
    }
    return render(request, 'posts/index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            
    context = {
        
    }
    return render(request, 'posts/index.html', context)

def delete(request, post_pk):
    return redirect('posts:detail', post_pk)

def detail(request, post_pk):
    context = {

    }
    return render(request, 'posts/detail.html', context)

def like(request, post_pk):
    pass

def comments_create(request, post_pk, comment_pk):
    pass

def comments_delete(request, post_pk, review_pk, comment_pk):
    pass

def comments_likes(request, post_pk, comment_pk):
    pass

def comments_update(request, post_pk, comment_pk):
    pass

def emotes(request, review_pk, emotion):
    pass

