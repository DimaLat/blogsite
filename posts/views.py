from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

from .forms import PostModelForm

from posts.models import Post
from .models import Author


def posts_list(request):
    posts = Post.objects.all() # взять все объекты, которые мы создали
    context = {
        'posts': posts # ключ значение для этого словаря, для всех постов
    }
    messages.info(request,'')
    return render(request, "posts/posts_list.html", context)


    # CRUD
    #Create retrieve update and delete

def posts_detail(request,slug):
        unique_post = get_object_or_404(Post,slug=slug)
        context = {
            'post':unique_post
        }
        messages.info(request,'This is the specific detail view.')

        return render(request, "posts/posts_detail.html", context)
    

def posts_create(request):
    author, created = Author.objects.get_or_create(
        user = request.user,
        email = request.user.email,
        cellphone_num = +375334343221
    )
    form = PostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.author = author
        form.save()
        messages.info(request,'Successfully created a new blog post.')

        return redirect('/posts')
    context = {
        'form':form
    }
    return render(request, "posts/posts_create.html", context)

def posts_update(request,slug):
        unique_post = get_object_or_404(Post,slug=slug)
        form = PostModelForm(request.POST or None,
                            request.FILES or None,
                            instance=unique_post)
        if form.is_valid():
            form.save()
            messages.info(request,'Blog updated successfully.')

            return redirect('/posts')


        context = {
            'form':form
        }
        return render(request, "posts/posts_update.html", context)


def posts_delete(request,slug):
    unique_post = get_object_or_404(Post,slug=slug)
    unique_post.delete()
    messages.info(request,'Post successfully deleted.')

    return redirect('/posts')



