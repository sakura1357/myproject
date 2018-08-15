from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class BlogType(models.Model):
	type_name = models.CharField(max_length = 20)

	def __str__(self):
		return self.type_name

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 50)
	blog_type = models.CharField(max_length = 30)
	content = RichTextUploadingField()
	author = models.CharField(max_length = 30)
	created_time = models.DateTimeField(auto_now_add = True)
	last_updated_time = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created_time']