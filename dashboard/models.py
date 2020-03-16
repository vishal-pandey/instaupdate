from django.db import models
from tinymce.models import HTMLField


class PostDetail(models.Model):
	post_detail = HTMLField()
	post_detail_title = models.CharField(blank=False, max_length=255)
	def __str__(self):
		return self.post_detail_title

class PostCategoryType(models.Model):
	post_category_name = models.CharField(blank=False, max_length=255)
	def __str__(self):
		return str(self.post_category_name)


class Category(models.Model):
	category_name = models.CharField(blank=False, max_length=255)
	def __str__(self):
		return str(self.category_name)



class Post(models.Model):
	p_type = models.IntegerField(blank=False)
	thumbnail = models.ImageField(upload_to='study_material', blank=True)
	title = models.CharField(blank=False, max_length=255)
	text_one = models.TextField(blank=False)
	text_two = models.TextField(blank=False)
	banner_image = models.ImageField(upload_to='study_material', blank=True)
	is_published = models.BooleanField(default=False)
	post_detail_id = models.ForeignKey(PostDetail, on_delete=models.CASCADE)
	post_category_type  = models.ForeignKey(PostCategoryType, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
	expiry_date = models.DateTimeField()

	def __str__(self):
		return str(self.title)



class PostCategory(models.Model):
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
	category_id = models.ForeignKey(Category, on_delete=models.CASCADE)




class Notification(models.Model):
	title = models.CharField(blank=False, max_length=255)
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.title)
