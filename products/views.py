from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ProductForm
from .models import Product
from posts.forms import CommentForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('products:detail', product.pk)
    else:
        form = ProductForm()
    context = {
        'product_form': form,
    }
    return render(request, 'products/create.html', context)

def update(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.user == product.user:
        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()        
                return redirect('products:detail', product.pk)
        else:
            form = ProductForm(nstance=product)
    else:
        return redirect('products:detail',product.pk)
    context = {
        'form':form,
        'product':product,
    }
    return render(request, 'products/upate.html', context)


def delete(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.user == product.user :
        product.delete()
    return redirect('products:detail', product_pk)

def detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    # comments = product.comment_set.all()
    # comment_form = CommentForm()
    context = {
        'product': product,
        # 'comment_form': comment_form,
        # 'comments': comments,
    }
    return render(request, 'products/detail.html', context)


def likes(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    if request.user in product.like_users.all():
        product.like_users.remove(request.user)
        is_liked = False
    else:
        product.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'product_likes_count': product.like_users.count(), #좋아요 수 표시
            }
    return JsonResponse(context)