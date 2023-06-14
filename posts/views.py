from django.shortcuts import render, redirect
from .forms import PostForm , CommentForm
from django.http import JsonResponse
from .models import Post, Emote , Comment
from taggit.models import Tag
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
def index_redirect(request):
    return render(request, 'posts/index.html')

def index(request):
    posts = Post.objects.all().order_by('-created_at')  # 전체 게시물 가져오기
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

# def create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         tags = request.POST.get('tags').split(',')
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#             for tag in tags:
#                 post.tags.add(tag.strip())
#             return redirect('posts:detail', post.pk)
#     else:
#         form = PostForm()
#     context = {
#         'post':post,
#     }
#     return render(request, 'posts/create.html', context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        tags = request.POST.get('tags', '').split(',')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            for tag in tags:
                post.tags.add(tag.strip())
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'post_form': form,
    }
    return render(request, 'posts/create.html', context)

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                post.tags.clear()
                tags = request.POST.get('tags').split(',')
                for tag in tags:
                    post.tags.add(tag.strip())
                return redirect('posts:detail', post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('posts:detail',post.pk)
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'posts/upate.html', context)

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user :
        post.delete()
    return redirect('posts:detail', post_pk)

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    tags = post.tags.all()
    comments = post.comment_set.all()
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'tags': tags,
    }
    return render(request, 'posts/detail.html', context)



def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user in post.like_post.all():
        post.like_post.remove(request.user)
        is_liked = False
    else:
        post.like_post.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'post_likes_count': post.like_post.count(), # 좋아요 개수 반환
    }
    return JsonResponse(context)

def comments_create(request, post_pk):
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
    if request.user in comment.like_comment.all():
        comment.like_comment.remove(request.user)
        is_liked = False
    else:
        comment.like_comment.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)

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
    return render(request, 'posts:detail', context)

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

def tagged(request, tag_pk):
    tag = Tag.objects.get(pk=tag_pk)
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'posts':posts,
    }
    return render(request, 'posts/tagged.html', context)

def search(request):
    query = None
    search_list = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        search_list = Post.objects.filter(
            Q(title__icontains=query) | Q(tags__name__icontains=query) # 제목 / 태그 검색
        ).distinct() # 검색 결과 중복 제거
    context = {
        'query': query,
        'search_list': search_list,
    }
    return render(request, 'posts/search.html', context)