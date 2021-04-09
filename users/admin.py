from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User

# Register your models here.


class UserAdminConfig(UserAdmin):
    model = User

    search_fields = ('email', 'username',)
    list_filter = ('is_superuser', 'is_staff', 'is_active',)
    ordering = ('email',)
    list_display = ('email', 'username', 'is_superuser',
                    'is_staff', 'is_active', 'date_joined',)

    fieldsets = (
        ('Personal', {
         'fields': ('email', 'username',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )


admin.site.register(User, UserAdminConfig)
