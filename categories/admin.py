from django.contrib import admin

from categories.models import Categories

# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass