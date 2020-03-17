from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response

import json
from .models import PostDetail, Category, Post, PostCategory, PostCategoryType

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import pytz
from django.utils import timezone


def post(request, mid):
	context = {}

	if PostDetail.objects.filter(id=mid).values('post_detail_title', 'post_detail'):
		qs = PostDetail.objects.filter(id=mid).values('post_detail_title', 'post_detail')[0]
		context['title'] = qs['post_detail_title']
		context['content'] = qs['post_detail']


		return render(request, 'dashboard/post.html', context);
	
	else:
		return render(request, 'dashboard/404.html')



def index(request):
	return render(request, 'dashboard/index.html')


def getCategories(request):
	print("Hlelo")
	data = list(Category.objects.filter().values('id', 'category_name'))
	return JsonResponse(data, safe=False)


@csrf_exempt
def postlist(request):

	if request.method == 'POST':
		print(datetime.now(tz=timezone.utc))
		q = {}
		if request.POST.get('category_ids'):
			category_ids = json.loads(request.POST.get('category_ids'))
			p_ids = [i['post_id'] for i in list(PostCategory.objects.filter(category_id__in=category_ids).values('post_id'))]
			q['id__in'] = p_ids

		if request.POST.get('post_ids'):
			p_ids = json.loads(request.POST.get('post_ids'))
			q['id__in'] = p_ids

		if request.POST.get('post_category_type_ids'):
			p_c_t_ids = json.loads(request.POST.get('post_category_type_ids'))
			q['post_category_type_id__in'] = p_c_t_ids

		if request.POST.get('is_expired'):
			if request.POST.get('is_expired') == '0':
				q['expiry_date__gte'] = datetime.now(tz=timezone.utc)
			elif request.POST.get('is_expired') == '1':
				q['expiry_date__lte'] = datetime.now(tz=timezone.utc)


		data = list(Post.objects.filter(**q).order_by('-created_on').values())
		return JsonResponse(data, safe=False)

	elif request.method == 'GET':
		data = list(Post.objects.filter(post_category_type_id = 1).values())
		return JsonResponse(data, safe=False)


def getPostCategoryType(request):
	data = list(PostCategoryType.objects.filter().values())
	print(data)
	return JsonResponse(data, safe=False)


