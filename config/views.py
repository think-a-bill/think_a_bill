from django.shortcuts import render, redirect
from posts.models import Post
from products.models import Product

def main(request):
    # posts = Post.objects
    # products = Product.objects

    # post_images = []
    # for post in posts[:5]:
    #     images = post_images.objects.filter(post=post)
    #     if images:
    #         post_images.append((post, images[0]))
    #     else:
    #         post_images.append((post,''))

    # product_images = []
    # for product in product[:5]:
    #     images = product_images.objects.filter(product=product)
    #     if images:
    #         product_images.append((product, images[0]))
    #     else:
    #         product_images.append((product,''))
            
    # context = {
    # 'post_images': post_images,
    # 'product_images': product_images,
    # }
    return render(request, 'main.html')