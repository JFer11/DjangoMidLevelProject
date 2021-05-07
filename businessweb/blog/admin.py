from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        # To return HTML code, have a look to
        # for https://stackoverflow.com/questions/47953705/how-do-i-use-allow-tags-in-django-2-0-admin
        return ", ".join([category.name for category in obj.categories.all()])

    post_categories.short_description = "Categories"


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
