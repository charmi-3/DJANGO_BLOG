from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import *
from .models import *
from .forms import *
from django.urls import reverse_lazy
# Create your views here.

class Home(ListView):
  model = Post
  template_name = 'posts/home.html'

def CreateBlog(request):
  if request.method=="POST" :
      form = AddBlog(request.POST)
      if form.is_valid() :
        if request.user.is_authenticated:
         Post = form.save(commit=False)
         Post.author = request.user
         Post.save()
         return redirect('home_page')
        else:
          return HttpResponse('You are not logged in')
  else:
    form = AddBlog(request.POST)
    return render(request,'posts/addpost.html',{'form':form})

class Detail(DetailView):
  model = Post
  template_name='posts/postdetail.html'

class Delete(DeleteView):
  model = Post
  template_name = 'posts/postdelete.html'
  success_url=reverse_lazy('home_page')

class Edit(UpdateView):
  model = Post
  fields = ('title','body')
  template_name = 'posts/postedit.html'
  success_url=reverse_lazy('home_page')