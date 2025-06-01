from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Personal

class CustomUserAdmin(UserAdmin):
    def save_model(self, request, obj, form, change):
        is_new = obj.pk is None
        super().save_model(request, obj, form, change)

        if obj.is_personal and not hasattr(obj, 'personal'):
            Personal.objects.create(
                user=obj,
                nome=obj.username,
                telefone='0000000000'
            )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Personal)
