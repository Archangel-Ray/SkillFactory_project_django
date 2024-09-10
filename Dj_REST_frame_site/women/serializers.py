from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = "__all__"

# class WomenSerializer(serializers.Serializer):
#     # прописываем все поля модели которая будет сериализоваться
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     # если передаются только данные, то запускается создание записи
#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     # если с данными передаётся ссылка на строку, то запускается изменение записи
#     # прописываются все поля, которые могут меняться
#     def update(self, instance, validated_data):
#         # instance - ссылка на объект модели "Women"
#         # validated_data - данные новой записи
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         # сохранение изменённой записи
#         instance.save()
#         return instance
