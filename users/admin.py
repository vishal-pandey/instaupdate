from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import UserPreference, UserBookmark, UserNotification

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class UserPreferenceInline(admin.TabularInline):
    model = UserPreference
    list_display = ['user_id', 'category_id']
    autocomplete_fields = ['category_id']

class UserBookmarkInline(admin.TabularInline):
    model = UserBookmark
    list_display = ['user_id', 'post_id']
    autocomplete_fields = ['post_id']

class UserNotificationInline(admin.TabularInline):
    model = UserNotification
    list_display = ['user_id', 'notification_id']
    autocomplete_fields = ['notification_id']




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'fname', 'lname', 'mobile', 'device_id', 'groups', 'user_permissions', ('date_joined', 'last_login'))}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_paid')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    inlines = [UserPreferenceInline, UserBookmarkInline, UserNotificationInline]




admin.site.register(CustomUser, CustomUserAdmin)