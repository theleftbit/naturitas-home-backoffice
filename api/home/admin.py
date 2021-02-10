from django.contrib import admin

# Register your models here.
from home.models import HomeSection, HomeSectionType, HomeSectionItem, HomeSectionItemType


@admin.register(HomeSectionType)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ('type', 'title', 'priority', 'images_path', 'deeplink_path')


@admin.register(HomeSectionItemType)
class HomeSectionItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(HomeSectionItem)
class HomeSectionItemAdmin(admin.ModelAdmin):
    list_display = ('section', 'naturitas_id', 'type', 'name', 'image_file_name', 'link_path')
    ordering = ('section__type__id',)
