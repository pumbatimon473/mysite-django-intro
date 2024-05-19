# A form of "Headless CMS": Admin Portal

from django.contrib import admin
from .models import User, Post

# Register your models here
# WAY 1:
admin.site.register(User)


# WAY 2: Custom Class - Provides more customization options
# @admin.register(Post)  # Register with annotation (preferred)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted', 'author')
    list_filter = ('date_posted', 'author')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)  # Registering without annotation
