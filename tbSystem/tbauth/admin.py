from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from tbauth.models.models import UserProfile
from tbauth.serializers.serializers import UserNameEmailSerializers

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("id",'email', 'first_name', 'last_name','is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'user', 'role')
    list_filter = ('role',)
    search_fields = ('email', 'user__email')
    autocomplete_fields = ['user']
  

admin.site.register(UserProfile, UserProfileAdmin)


