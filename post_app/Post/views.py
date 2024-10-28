from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.

def home(request):

    posts = Post.objects.all()
    context = {'posts': posts}
    # return render(request, 'post/home.html', context)
    return render(request, 'post/home.html', context)

def about(request):
    return render(request, 'about.html')
#     return render(request, 'Post/templates/blog/about.html')


def end(request):
    return HttpResponse("На этом всё!")


def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'post/post_form.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'post/post_form.html', {'form': form})
