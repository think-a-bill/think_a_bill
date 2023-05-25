from django.shortcuts import render, redirect
from .forms import PostForm , CommentForm
from django.http import JsonResponse
from .models import Post, Emote , Comment


# Create your views here.
def index_redirect(request):
    return redirect('index')

def index(request):
    context = {
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            
    context = {
        'post':post,
    }
    return render(request, 'posts/index.html', context)

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:detail', post.pk)
        else:
            form = PostForm()
    else:
        return redirect('posts:detail',post.pk)
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'posts/upate.html')
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user :
        post.delete()
    return redirect('posts:detail', post_pk)

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = post.comment_set.all()
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'posts/detail.html', context)


def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'post_likes_count': post.like_users.count(), #좋아요 수 표시
    }
    return JsonResponse(context)

def comments_create(request, post_pk, comment_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('posts:detail', post_pk=post_pk)
    else:
        Comment_form = CommentForm()
    return redirect('posts:detail', post_pk=post_pk)



def comments_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('posts:detail', post_pk)

def comments_likes(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user in comment.like_users.all():
        comment.like_user.remove(request.user)
        comment_is_liked = False
    else:
        comment.like_users.add(request.user)
        comment_is_liked = True
    context = {
        'comment_is_liked': comment_is_liked,
        'post_comment_likes_count': comment.like_users.count(), #좋아요 수 표시
    }
def comments_update(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    post = Post.objects.get(pk=post_pk)
    if request.user == comment.user:
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('posts:detail', post.pk)
        else:
            form = CommentForm(instance=comment)
    else:
        return redirect('posts:detail', post.pk)
    context = {
        'form':form,
        'comment':comment,
    }
    return render(request, 'posts:detail', post.pk)

EMOTIONS = [
    {'label': '유용해요', 'value': 1},
    {'label': '별로에요', 'value': 2},
]

def emotes(request, post_pk, emotion):
    post = Post.objects.get(pk=post_pk)
    filter_query = Emote.objects.filter(
        post=post,
        user=request.user,
        emotion=emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        Emote.objects.create(post=post, user=request.user, emotion=emotion)

    return redirect('posts:detail', post_pk)

