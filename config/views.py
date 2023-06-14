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
    # return render(request, 'main.html')
    recent_posts = Post.objects.order_by('-created_at')[:5]  # 최근 5개의 게시글 가져오기
    recent_products = Product.objects.order_by('-created_at')[:5]  # 최근 5개의 게시글 가져오기
    context = {
        'recent_posts': recent_posts,
        'recent_products': recent_products
        }
    return render(request, 'main.html', context)