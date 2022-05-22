from django.contrib import admin
from .models import AlbumM,PostCategory,mkSelectM
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin


class AlbumMAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(AlbumM,AlbumMAdmin)
admin.site.register(PostCategory)
admin.site.register(mkSelectM)