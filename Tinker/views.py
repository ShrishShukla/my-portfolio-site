from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
# Create your views here.

posts = [
	
			{'author': 'dsfvkvdxc'
			},
			{'author': 'iogmpkodfcb'
			}
		]
def home(request):
	context = {'posts' : posts}
	return render(request, 'Tinker/home.html', context)

class PostListView(ListView):
	model = Post
	template_name='Tinker/home.html'
	context_object_name='posts'
	ordering = ['-date_posted']


class PostDetailView(DetailView):
	model = Post
	
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title' , 'content', 'image']
	login_url = 'login'
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title' , 'content']

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

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'Tinker/about.html')
