from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import strip_tags

# 博客类型
class BlogType(models.Model):
	type_name = models.CharField(max_length = 20)

	def __str__(self):
		return self.type_name


# 博客标记（技术杂谈|随心而记）
class BlogMark(models.Model):
	mark_name = models.CharField(max_length = 20)

	def __str__(self):
		return self.mark_name

# Create your models here.
class Blog(models.Model):
	# 标题
	title = models.CharField(max_length = 50)
	# 博客类型
	blog_type = models.CharField(max_length = 30)
	# 博客内容
	content = RichTextUploadingField()
	# 博客摘要，用于博客列表页面显示
	excerpt = models.CharField(max_length = 200, blank = True)
	# 作者 
	author = models.CharField(max_length = 30)
	# 博客创建时间
	created_time = models.DateTimeField(auto_now_add = True)
	# 博客最后一次更新时间
	last_updated_time = models.DateTimeField(auto_now_add = True)
	# 博客标记（区分技术杂谈和随心而记）
	blog_mark = models.ForeignKey(BlogMark, on_delete = models.CASCADE)

	def __str__(self):
		return self.title
	# 复写父类的save方法，将博客内容的前120个字符作为摘要内容。
	# 判断博客类型是否存在，如未存在，则存入BlogType表
	def save(self, *args, **kwargs):
		if not self.excerpt:
			self.excerpt = strip_tags(self.content)[:120]
		if not BlogType.objects.filter(type_name = self.blog_type).exists():
			blog_type = BlogType()
			blog_type.type_name = self.blog_type
			blog_type.save()
		super(Blog, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-created_time']

