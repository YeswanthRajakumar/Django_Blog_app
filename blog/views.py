from django.shortcuts import render, get_object_or_404
# for Accessing values from post database
from blog.models import Post

from .models import User

# for using class-based-views
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

# it is setting  some restrictions for class-based-views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.conf import settings

# Create your views here.

'''
def home(request):
    context = \
        {
            'posts': Post.objects.all()
        }
    return render(request, 'blog/home.html', context)'''


# class-based-view for home
class Post_List_View(ListView):
    # model is specified ,so that ListView can query this model
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<view-type>.html ------> here blog/post_list.html
    context_object_name = 'posts'
    # for  ordering the query(ORDER_BY)
    ordering = ['-posted_time']
    paginate_by = 5


# class-based-view for display all post by particular user
class Users_all_Post_List_View(ListView):
    # model is specified ,so that ListView can query this model
    model = Post
    template_name = 'blog/users_all_post.html'  # <app>/<model>_<view-type>.html ------> here blog/post_list.html
    context_object_name = 'posts'
    # for  ordering the query(ORDER_BY)
    paginate_by = 5

    # for querying from URL, In our case if user is not found it returns 404
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        print(user)
        return Post.objects.filter(author=user).order_by('-posted_time')


# class-based-view for view a single post
class Post_Detail_View(DetailView):
    # model is specified ,so that ListView can query this model
    model = Post


# class-based-view for creating a post
class Post_Create_View(LoginRequiredMixin, CreateView):
    # model is specified ,so that ListView can query this model
    model = Post
    fields = ['title', 'post_content']

    # This method is set author to post automatically by setting current user to form instance's author before validation

    def form_valid(self, form):
        # setting current user to form instance 's author
        form.instance.author = self.request.user
        return super().form_valid(form)


# class-based-view for Updating a post
class Post_Update_View(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # model is specified ,so that ListView can query this model
    model = Post
    fields = ['title', 'post_content']

    # This method is set author to post automatically by setting current user to form instance's author before validation

    def form_valid(self, form):
        # setting current user to form instance 's author
        form.instance.author = self.request.user
        return super().form_valid(form)

    # This method checks whether the author only allowed to edit his post
    def test_func(self):
        current_post = self.get_object()
        if self.request.user == current_post.author:
            return True
        return False


# class-based-view for Delete a single post
class Post_Delete_View(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # model is specified ,so that ListView can query this model
    model = Post
    success_url = '/blog/'

    # This method checks whether the author only allowed to edit his post
    def test_func(self):
        current_post = self.get_object()
        if self.request.user == current_post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')
