from django.contrib import admin
from dashboard.models import PostDetail, PostCategoryType, Category, Post, PostCategory, Notification
from django.forms import ModelForm
from django import forms
from django.utils.html import format_html

class PostDetailAdmin(admin.ModelAdmin):
	model = PostDetail
	list_display = ['id', 'post_detail', 'post_detail_title', 'show_post_detail_url']
	search_fields = ['id', 'post_detail', 'post_detail_title']

	def show_post_detail_url(self, obj):
		return format_html("<a href='/{url}' target='_blank'>post link</a>", url=obj.id, title=obj.post_detail_title)

	show_post_detail_url.short_description = "Post Detail URL"

	


class PostCategoryTypeAdmin(admin.ModelAdmin):
	model = PostCategoryType
	list_display = ['id', 'post_category_name']
	search_fields = ['id', 'post_category_name']


class CategoryAdmin(admin.ModelAdmin):
	model = Category
	list_display = ['id', 'category_name']
	search_fields = ['id', 'category_name']


class PostCategoryInline(admin.TabularInline):
	model = PostCategory
	list_display = ['post_id', 'category_id']
	search_fields = ['post_id__title', 'category_id__category_name']
	autocomplete_fields = ['category_id']


class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ['id', 'p_type', 'thumbnail', 'title', 'text_one', 'text_two', 'banner_image', 'is_published', 'post_detail_id', 'post_category_type', 'created_on', 'expiry_date']
	search_fields = ['id', 'p_type', 'title', 'text_one', 'text_two', 'post_detail_id', 'post_category_type', 'created_on', 'expiry_date']
	autocomplete_fields = ['post_detail_id', 'post_category_type']
	inlines = [PostCategoryInline]


class NotificationAdmin(admin.ModelAdmin):
	model = Notification
	list_display = ['id', 'title', 'post_id']
	search_fields = ['id', 'title', 'post_id__title']
	autocomplete_fields = ['post_id']





admin.site.register(Notification, NotificationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PostCategoryType, PostCategoryTypeAdmin)
admin.site.register(PostDetail, PostDetailAdmin)
