from unicodedata import category
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    featured_post = Post.objects.all()
    page = Paginator(featured_post, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {'page':page}
    return render(request, 'core/index.html', context)



def PostDetail(request,pk):
    post_detail = Post.objects.filter(pk=pk)
    context = {'post_detail':post_detail}
    return render(request, 'core/post_detail.html', context)
