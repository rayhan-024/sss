from django.core import paginator
from django.shortcuts import render, get_object_or_404
from .models import Post ,Category
from django.db.models import Count
from .forms import CommentFrom
from django.http.response import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def blog_list(request):
    
    #categories = Category.objects.all()
    posts = Post.objects.all()
    
    categories = Category.objects.all().annotate(posts_count=Count('posts'))
    
    latest_post = Post.objects.all()[:3]

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    context = {
       'posts': posts,
       'latest_post': latest_post,
       'categories': categories,
       'page_obj': page_obj
    }

    return render(request, 'blog/index.html', context)

def blog_details(request, slug):
    categories = Category.objects.all().annotate(posts_count=Count('posts'))
    latest_post = Post.objects.all()[:3]

    post = Post.objects.get(slug=slug)
    similar_post = post.tags.similar_objects()[:4]
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentFrom(request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)

            new_comment.post = post
            new_comment.save()
            # Redirect in a new url

            messages.success(request, 'Your comment submitted.')
            return HttpResponseRedirect(request.path_info)

            # If a got or any other method we'll create a blank form
    
    else :
        comment_form = CommentFrom()

    context  = {
        'post' : post,
        'similar_post' : similar_post,
        'latest_post': latest_post,
        'categories': categories,        
        'comments': comments,

    }

    return render(request, 'blog/details.html', context)
    
def search_blog(request):

    categories = Category.objects.all().annotate(posts_count=Count('posts'))
    latest_post = Post.objects.all()[:3]

    queryset = Post.objects.all()
    query = request.GET.get('q')
    
    # paginator = Paginator(queryset, 1)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) | Q(short_desc__icontains=query) |
            Q(description__icontains=query)


        ).distinct()
    context = {
        'queryset': queryset,
        'latest_post': latest_post,
        'categories': categories,
        'query': query

    }
    return render(request, 'blog/search.html', context)

def category(request, category_slug=None):

    category = None
    categories = Category.objects.all().annotate(posts_count=Count('posts'))
    posts = Post.objects.all()
    
    latest_post = Post.objects.all()[:3]

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
        
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    
    
    context = {
       'posts': posts,
       'latest_post': latest_post,
       'category': category,
       'categories': categories,
       'page_obj': page_obj
    }

    return render(request, 'blog/category.html', context)