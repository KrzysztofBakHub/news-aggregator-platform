from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.select_related("source", "category").all()
    serializer_class = ArticleSerializer
