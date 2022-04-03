from django.contrib import admin

from recipes.models import Category, Recipe


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)


class RecipiAdmin(admin.ModelAdmin):
    ...


admin.site.register(Recipe, RecipiAdmin)
