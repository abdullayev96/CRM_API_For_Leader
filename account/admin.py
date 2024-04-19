from django.contrib import admin
from .models import User

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from profiles.models import UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
    (None, {'fields': ('email', 'password')}),
    (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    'groups', 'user_permissions')}),
    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
    (None, {
    'classes': ('wide',),
    'fields': ('email', 'password1', 'password2'),
    }),
      )
    list_display = ['id','email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']
    inlines = (UserProfileInline, )


#
#
#
# class CustomUserAdmin(UserAdmin):
#
#     list_display  = ['id','username', 'email','password','staff', 'active']
#     list_filter = ['email','password', 'staff', 'active']
#
#
#     search_fields = ["email","full_name"]
#     ordering = ("email",)
#
#
# admin.site.register(CustomUser, CustomUserAdmin)





