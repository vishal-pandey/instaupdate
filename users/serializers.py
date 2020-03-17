from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', 'groups', 'email', 'is_staff', 'is_active', 'date_joined', 'mobile', 'device_id', 'is_paid', 'fname', 'lname', ]



     
     
     
     
     
     
     
     
