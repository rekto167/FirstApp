from django.contrib import admin

# Register your models here.
from .models import MenuModel


class ChefAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]


admin.site.register(MenuModel)
