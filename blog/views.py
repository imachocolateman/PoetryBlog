from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

from .models import Post

# Create your views here.
def post_list(request, tag_slug=None):
	latest_post_list = Post.objects.order_by('-post_date')[:5]
	# posts = get_object_or_404(Post)

	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		# posts = Post.objects.filter(tags__in=[tag])

	context = {
		'latest_post_list': latest_post_list,
		# 'posts': posts,
		'tag': tag,
	}

	return render(request, 'blog/list.html', context)

def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {
		"post": post
	}
	return render(request, 'blog/detail.html', context)
