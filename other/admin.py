from django.contrib import admin
from other.models import MetaData, UserDeviceData



class MetaDataAdmin(admin.ModelAdmin):
	model = MetaData
	list_display = ['key', 'value']
	search_fields = ['key', 'value']


class UserDeviceDataAdmin(admin.ModelAdmin):
	model = MetaData
	list_display = ['device_id', 'firebase_id', 'user_id']
	search_fields = ['device_id', 'firebase_id', 'user_id']


admin.site.register(MetaData, MetaDataAdmin)
admin.site.register(UserDeviceData, UserDeviceDataAdmin)