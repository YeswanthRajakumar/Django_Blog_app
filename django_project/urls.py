from django.contrib import admin
from django.urls import path, include

# for  Login and Logout we are using predef views
from django.contrib.auth import views as auth_views

# for creating routing for user_app
from user import views as user_views

# for serving files upload by the user especially media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('register/', include('user.urls')),
    path('profile/', user_views.profile, name='user-profile'),

    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
