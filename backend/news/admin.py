from django.contrib import admin
from .models import Article, Category, Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "source", "category", "published_at", "created_at")
    list_filter = ("source", "category", "published_at")
    search_fields = ("title", "description")
    ordering = ("-published_at",)