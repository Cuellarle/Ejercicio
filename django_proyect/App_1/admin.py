from django.contrib import admin
from .models import Menu,Logger	,Persona
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Logger)
admin.site.register(Menu)
#admin.site.register(Persona)
admin.site.unregister(User)
# Register your models here.

@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]

def get_form(self, request, obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    is_superuser = request.user.is_superuser

    if not is_superuser:
        form.base_fields['username'].disabled = True
        form.base_fields['is_staff'].disabled = True
        form.base_fields['is_superuser'].disabled = True
        form.base_fields['user_permissions'].disabled = True
        form.base_fields['groups'].disabled =   True
        form.base_fields['password'].disabled =   True

    return form

@admin.register(Persona)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('apellidos', 'nombres')
    search_fields = ('apellidos_startswith',)