from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('UNISEX/', views.UNISEX, name='UNISEX'),
    path('comment/', views.comment, name='comment'),
    path('<int:comment_id>/', views.comment_detail, name='comment_detail'),
    path('detail/<int:post_id>/', views.post_detail, name='post_detail'),
    path('search', views.search, name='search'),
    path('login/', auth_views.LoginView.as_view(template_name='polls/Login.html'), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('signup/', views.signup, name='signup'),
]
