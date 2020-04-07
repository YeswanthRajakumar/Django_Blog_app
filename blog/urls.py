from django.urls import path, include

from . import views

from blog.views import (Post_List_View,
                        Users_all_Post_List_View,
                        Post_Detail_View,
                        Post_Create_View,
                        Post_Update_View,
                        Post_Delete_View)

urlpatterns = [
    # path('', views.home, name='blog-home'),
    # class-based-view for homepage
    path('', Post_List_View.as_view(), name='blog-home'),

    # class-based-view for homepage
    path('post/<str:username>/', Users_all_Post_List_View.as_view(), name='users-all-posts'),

    # class-based-view routing for view a single post
    path('post/<int:pk>/', Post_Detail_View.as_view(), name='post-detail'),

    # class-based-view  routing for create a  post
    path('post/new', Post_Create_View.as_view(), name='post-new'),
    # for insert and update template_name should be <model>_form.html -----> Here post_form.html

    # class-based-view routing  for update a post
    path('post/<int:pk>/update/', Post_Update_View.as_view(), name='post-update'),

    # class-based-view routing  for delete a post
    path('post/<int:pk>/delete/', Post_Delete_View.as_view(), name='post-delete'),

    path('about/', views.about, name='blog-about'),
]
