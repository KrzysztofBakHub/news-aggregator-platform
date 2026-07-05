from rest_framework import serializers
from .models import Article, Category, Source

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name', 'url']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ArticleSerializer(serializers.ModelSerializer):
    source = SourceSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "description",
            "url",
            "source",
            "category",
            "published_at",
            "created_at",
        ]