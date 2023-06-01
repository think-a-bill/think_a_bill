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
            form = ProductForm(instance=product)  
    else:
        return redirect('products:detail', product.pk)
    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'products/update.html', context)



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
    if request.user in product.like_product.all():
        product.like_product.remove(request.user)
        is_liked = False
    else:
        product.like_product.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'product_likes_count': product.like_product.count(),
    }
    return JsonResponse(context)


# 상품 리스트 
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/product_list.html', context)