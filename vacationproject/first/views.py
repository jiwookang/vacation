from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 4)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 posts변수에 담고 return 해준다.
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})

def write(request):
    return render(request, 'write.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        blog.title = title
        blog.body = body
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('detail', blog.id)
    
    return render(request, 'edit.html', {'blog': blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('home')

