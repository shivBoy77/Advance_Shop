from django.contrib import admin

from .models import BlogCategories, Blog, Author, NewsLetterUser

admin.site.register(Author)
admin.site.register(BlogCategories)
admin.site.register(Blog)


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)


admin.site.register(NewsLetterUser, NewsLetterAdmin)
