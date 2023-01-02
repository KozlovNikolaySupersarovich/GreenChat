from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'status']
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('status',)}),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        form.base_fields["status"].required = False
        return form


admin.site.register(CustomUser, CustomUserAdmin)
