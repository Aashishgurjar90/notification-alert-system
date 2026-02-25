from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):

    model = User

    # IMPORTANT: tenant and role ko add form me include karo
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'tenant', 'role'),
        }),
    )

    # Edit form ke liye
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Tenant Info', {'fields': ('tenant', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    list_display = ('username', 'tenant', 'role', 'is_staff')


admin.site.register(User, CustomUserAdmin)