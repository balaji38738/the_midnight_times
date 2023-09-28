from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=30)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=80)
    source_id = serializers.CharField(max_length=30, source="id")
    source_name = serializers.CharField(max_length=30, source="name")
    article_url = serializers.CharField(source="url")
    image_url = serializers.CharField(source="urlToImage")
    description = serializers.CharField()
    date_published = serializers.DateTimeField(source="publishedAt")