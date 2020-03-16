from django.conf.urls import url
from dashboard import views
# SET THE NAMESPACE!
app_name = 'dashboard'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^(?P<mid>[\w-]+)/$',views.index,name='index'),
]