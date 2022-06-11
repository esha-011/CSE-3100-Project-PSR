from dataclasses import fields
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView
from regex import template
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'psr/home.html' ,context)


class PostListView(ListView):
    model = Post
    template_name = 'psr/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView( LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
           return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
           return True
        return False

def about(request):
    return render(request, 'psr/about.html')   

def members(request):
    return render(request, 'psr/members.html')  

def contact(request):
    return render(request, 'psr/contact.html')  

# def signup(request):
#     if request.method == 'POST':
#         # Get the post parameters
#         username = request.post['username']
#         fname = request.post['fname']
#         lname = request.post['lname']
#         email = request.post['email']
#         pass1 = request.post['pass1']
#         pass2 = request.post['pass2']

#         # create the users
#         myuser = User.objects.create_user(username,email,pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname

#         messages.success(request,"Your acccount is created successfully !")
#         return redirect('psr-home')
#     else:
#         return HttpResponse('404- NOT FOUND') 