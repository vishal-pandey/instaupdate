from django.urls import include, path
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('users/register', views.create_auth),
    path('bookmark/', views.UserBookmarkView.as_view()),
    path('notification/', views.UserNotificationView.as_view()),
    path('preference/', views.UserPreferenceView.as_view()),
    path('checkphone/', views.checkPhone, name='checkphone')
]