from django.shortcuts import render, get_object_or_404
from taggit.models import Tag

from .models import Post

# Create your views here.
def post_list(request, tag_slug=None):
	latest_post_list = Post.objects.order_by('-post_date')[:5]
	# Filter these Tags by most used
	all_tags = Tag.objects.all()

	tag = None
	if tag_slug:
		tag = get_object_or_404(Tag, slug=tag_slug)
		latest_post_list = Post.objects.filter(tags__name=tag_slug)


	context = {
		'latest_post_list': latest_post_list,
		'tag': tag,
		'tags': all_tags,
	}
	return render(request, 'blog/list.html', context)


def detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {
		"post": post
	}
	return render(request, 'blog/detail.html', context)
