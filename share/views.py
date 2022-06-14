from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# Create your views here.

def home(request):
    context={'posts':Post.objects.all()}
    return render(request, 'share/home.html',context)

class PostListView(ListView):
    template_name='share/home.html'
    ordering=['-date_posted']
    context_object_name='posts'
    model=Post

class PostDetailView(DetailView):
    model=Post 
    template_name='share/detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)  

def about(request):
    return render(request,'share/about.html',{'title':'about'})    