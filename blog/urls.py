from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
	path('', views.post_list, name='list'),
	path('<int:post_id>/', views.detail, name='detail'),
	path('tag/<slug:tag_slug>/', views.post_list, name='post_tag'),
]