from django.contrib import admin

from .models import Youtuber
# Register your models here.
from django.utils.html import format_html


class YtAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src="{}" width="40"  />',format(object.photo.url))

    list_display=('id','name','myphoto','subs_count','is_featured')
    search_fields=('name','camera_type')
    list_filter=('city','camera_type')
    list_display_links=('id','name')
    list_editable=('is_featured',)

admin.site.register(Youtuber,YtAdmin)