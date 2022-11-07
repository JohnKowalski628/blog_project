from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('about/', views.AboutView.as_view(), name='about'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]
