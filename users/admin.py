from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

# Register your models here.


class UserAdminConfig(UserAdmin):
    model = User

    search_fields = ('email', 'username',)
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'city')
    ordering = ('email',)
    list_display = ('email', 'username', 'city', 'is_superuser',
                    'is_staff', 'is_active', 'date_joined',)

    fieldsets = (
        ('Personal', {
         'fields': ('email', 'username', 'city')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'city', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(User, UserAdminConfig)
