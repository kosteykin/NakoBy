from django.contrib import admin

from news.models import Post


class NewsPost(admin.ModelAdmin):
    list_display = ('post_title', 'post_publication_date', 'post_category', 'post_author')


admin.site.register(Post, NewsPost)
