from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.Serializer):
    # прописываем все поля модели которая будет сериализоваться
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    # создание записи в модели
    def create(self, validated_data):
        return Women.objects.create(**validated_data)
