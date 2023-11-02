from django.contrib import admin

from app.models import Blogger


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    pass
