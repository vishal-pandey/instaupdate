from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from django.conf.urls.static import static
from rest_framework.authtoken import views
from users.views import CustomAuthToken
from django.conf import settings
from dashboard import views as dviews


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', CustomAuthToken.as_view()),
    url(r'^user/', include('users.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns.append(url(r'', dviews.index,name='index'))

admin.site.site_header = 'Insta Update'