from django.shortcuts import render

from django.contrib.auth.models import Group
from .models import CustomUser, UserBookmark, UserNotification, UserPreference
from dashboard.models import Category, Post, Notification

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomUserSerializer
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.views import APIView
import json

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'email': user.email,
            'email': user.email, 
			'is_staff': user.is_staff, 
			'is_active': user.is_active, 
			'date_joined': user.date_joined, 
			'mobile': user.mobile, 
			'device_id': user.device_id, 
			'is_paid': user.is_paid, 
			'fname': user.fname, 
			'lname': user.lname, 
        })

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]

class UserBookmarkView(APIView):

    def get(self, request, format=None):
        return Response(list(UserBookmark.objects.filter(user_id=request.user).values('post_id')))

    def post(self, request, format=None):
        post_ids = json.loads(request.data['post_ids'])
        for p_id in post_ids:
            try:
                the_post = Post.objects.get(pk=p_id)
                if UserBookmark.objects.filter(user_id=request.user, post_id=the_post):
                    pass
                else:
                    UserBookmark.objects.create(user_id=request.user, post_id=the_post)
            except Exception as e:
                print(e)

        return Response(list(UserBookmark.objects.filter(user_id=request.user).values('post_id')))


    def delete(self, request, format=None):
        post_ids = json.loads(request.data['post_ids'])
        for p_id in post_ids:
            try:
                the_post = Post.objects.get(pk=p_id)
                if UserBookmark.objects.filter(user_id=request.user, post_id=the_post):
                    UserBookmark.objects.filter(user_id=request.user, post_id=the_post).delete()
            except Exception as e:
                print(e)

        return Response(list(UserBookmark.objects.filter(user_id=request.user).values('post_id')))

class UserNotificationView(APIView):

    def get(self, request, format=None):
        return Response(list(UserNotification.objects.filter(user_id=request.user).values('notification_id')))

    def post(self, request, format=None):
        notification_ids = json.loads(request.data['notification_ids'])
        for n_id in notification_ids:
            try:
                the_notification = Notification.objects.get(pk=n_id)
                if UserNotification.objects.filter(user_id=request.user, notification_id=the_notification):
                    pass
                else:
                    UserNotification.objects.create(user_id=request.user, notification_id=the_notification)
            except Exception as e:
                print(e)

        return Response(list(UserNotification.objects.filter(user_id=request.user).values('notification_id')))

    def delete(self, request, format=None):
        notification_ids = json.loads(request.data['notification_ids'])
        for n_id in notification_ids:
            try:
                the_notification = Notification.objects.get(pk=n_id)
                if UserNotification.objects.filter(user_id=request.user, notification_id=the_notification):
                    UserNotification.objects.filter(user_id=request.user, notification_id=the_notification).delete()
            except Exception as e:
                print(e)

        return Response(list(UserNotification.objects.filter(user_id=request.user).values('notification_id')))

class UserPreferenceView(APIView):

    def get(self, request, format=None):
        return Response(list(UserPreference.objects.filter(user_id=request.user).values('category_id')))

    def post(self, request, format=None):
        category_ids = json.loads(request.data['category_ids'])
        for c_id in category_ids:
            try:
                the_category = Category.objects.get(pk=c_id)
                if UserPreference.objects.filter(user_id=request.user, category_id=the_category):
                    pass
                else:
                    UserPreference.objects.create(user_id=request.user, category_id=the_category)
            except Exception as e:
                print(e)

        return Response(list(UserPreference.objects.filter(user_id=request.user).values('category_id')))


    def delete(self, request, format=None):
        category_ids = json.loads(request.data['category_ids'])
        for c_id in category_ids:
            try:
                the_category = Category.objects.get(pk=c_id)
                if UserPreference.objects.filter(user_id=request.user, category_id=the_category):
                    UserPreference.objects.filter(user_id=request.user, category_id=the_category).delete()
            except Exception as e:
                print(e)

        return Response(list(UserPreference.objects.filter(user_id=request.user).values('category_id')))


