from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import PostDetail

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


# Create your views here.
