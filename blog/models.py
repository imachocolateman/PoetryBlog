import datetime

from django.db import models
from django.utils import timezone

from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	post_date = models.DateTimeField('date published')
	content = models.TextField(default="Add content here")
	last_update = models.DateTimeField(auto_now=True)
	tags = TaggableManager()
	snippet = models.CharField(max_length=200, default="Add Snippet here")
	image = models.ImageField(blank=True, upload_to='blog_images')
	


	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.post_date >= timezone.now() - datetime.timedelta(days=1)

	def was_updated_recently(self):
		return self.last_update >= timezone.now() - datetime.timedelta(days=1)

		