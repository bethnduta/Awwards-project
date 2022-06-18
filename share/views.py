from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from share.serializer import PostSerializer


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

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False     


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form) 


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post 
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False 

def about(request):
    return render(request,'share/about.html',{'title':'about'})   

def search(request):
    if request.method == "POST": 
        searched = request.POST['searched']
        post=Post.objects.filter(title__icontains=searched).all()
        return render(request,'share/search.html',{'post':post,'searched':searched})
    else:
         return render(request,'share/search.html')        


class PostView(APIView):
     #APIView as a base class for our API view function.
    def get(self, request, format=None):
        #define a get method where we query the database to get all the MoringaMerchobjects
        all_post = Post.objects.all()
        #serialize the Django model objects and return the serialized data as a response.
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        # post method will be triggered when we are getting form data
        serializers = PostSerializer(data=request.data)
        # serialize the data in the request
        if serializers.is_valid():
            # If valid we save the new data to the database and return the appropriate status code.
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    
  


                