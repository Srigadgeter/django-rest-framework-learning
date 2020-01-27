from django.contrib import admin

from .models import UserProfile, ProfileFeedItem


class UserProfileAdmin(admin.ModelAdmin):
    list_display=['email', 'name', 'is_active', 'is_superuser', 'is_staff']


class ProfileFeedItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_profile', 'status_text']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProfileFeedItem, ProfileFeedItemAdmin)