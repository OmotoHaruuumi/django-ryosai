from django.contrib import admin
from . import models
from import_export import resources  
from import_export.admin import ImportExportModelAdmin
from .models import Pro

class ProResource(resources.ModelResource):

    class Meta:
        model = Pro
        import_id_fields = ('name',)
        fields = ("name","body","place","image")

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Pro)
class ProAdmin(ImportExportModelAdmin):
      resource_class = ProResource