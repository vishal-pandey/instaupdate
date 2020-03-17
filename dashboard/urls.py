from django.conf.urls import url
from dashboard import views
# SET THE NAMESPACE!
app_name = 'dashboard'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'post-categories/', views.getPostCategoryType, name='getPostCategoryType'),
    url(r'categories/', views.getCategories, name='getCategories'),
    url(r'postlist/', views.postlist, name='postlist'),
    url(r'^(?P<mid>[\w-]+)/$',views.post,name='post'),
    # url(r'',views.index,name='index'),
]