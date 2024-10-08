"""
документация по классам представлений
https://www.django-rest-framework.org/api-guide/generic-views/
"""
from rest_framework import generics, mixins
from rest_framework.decorators import action
# настройка разбивки на страницы
from rest_framework.pagination import PageNumberPagination
# документация по классам ограничений: https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer


# не подключён. оставлен на память:
# универсальный класс. виды запросов по отдельности.
# можно выбрать конкретный функционал класса
class WomenViewSet(mixins.CreateModelMixin,  # добавление записи
                   mixins.RetrieveModelMixin,  # возвращает запись
                   mixins.UpdateModelMixin,  # меняет запись
                   mixins.DestroyModelMixin,  # удаляет запись
                   mixins.ListModelMixin,  # возвращает список записей
                   GenericViewSet):  # отображение функционала
    """
    описание универсальных классов:
    https://www.django-rest-framework.org/api-guide/viewsets/#viewsets
    """
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # в этом методе можно прописывать логику если она необходима
    def get_queryset(self):
        pk = self.kwargs.get("pk")  # если ключ был передан, то необходима конкретная запись
        if not pk:
            return Women.objects.all()[:10]
        return Women.objects.filter(pk=pk)  # возвращаться должен обязательно список

    # добавление пути в маршрутизатор
    @action(  # декоратор для создания нового маршрута
        methods=['get'],  # список методов
        detail=False  # отображение одной строки базы - True. если False, то все
    )
    def categories(self, request):  # имя префикса пути берётся по названию метода
        cats = Category.objects.all()
        return Response({'cats': [c.name for c in cats]})

    # получение конкретной записи
    @action(methods=['get'], detail=True)
    def category(self, request, pk):
        cat = Category.objects.get(pk=pk)
        return Response({'cat': cat.name})


# собственный класс разбивки на страницы
# документация https://www.django-rest-framework.org/api-guide/pagination/#pagenumberpagination
class WomenAPIListPagination(PageNumberPagination):
    page_size = 2  # количество записей на странице
    page_size_query_param = 'page_size'  # индивидуальное количество страниц. указывается после амперсанда в запросе
    max_page_size = 100  # максимальное количество страниц индивидуальной настройки


# вернулись к этому классу для демонстрации авторизации:
# возвращает список записей по GET запросу и отправляет POST запрос
class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = WomenAPIListPagination


# вернулись к этому классу для демонстрации авторизации:
# заменяет запись
class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


# для демонстрации авторизации:
# удаляет запись
class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)


# этот класс не подключён. оставлен на память:
# класс всех запросов
class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# этот класс не подключён
# оставлен на память: как прописывать представления самостоятельно
class WomenAPIView(APIView):  # наследуемся от базового класса
    # обработчик GET запросов
    def get(self, request):
        query_of_all_data = Women.objects.all()  # сохраняем Queryset
        # в сериализатор отправляется Queryset и указывается,
        # что будет преобразовываться несколько записей
        # возвращается коллекция из сериализатора
        return Response({'posts': WomenSerializer(query_of_all_data, many=True).data})

    # обработчик POST запросов
    def post(self, request):
        # через сериализатор запрос преобразуется в объект понятный этой программе
        # в переменной сохраняются данные из этого запроса
        serializer = WomenSerializer(data=request.data)
        # проверка полученных данных
        serializer.is_valid(raise_exception=True)
        # метод сохранения запускает в сериализаторе метод создания записи в базе
        serializer.save()
        # возвращаются данные из объекта
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        # получает ключ записи
        pk = kwargs.get("pk", None)
        # проверяет ключ
        if not pk:
            return Response({"error": "Метод PUT не определён"})

        # пробует получить запись по ключу
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Объект не найден"})

        # если запись получена передаём в сериализатор данные из запроса и эту запись
        serializer = WomenSerializer(data=request.data, instance=instance)
        # проверка полученных данных
        serializer.is_valid(raise_exception=True)
        # метод сохранения запускает в сериализаторе метод обновления записи в базе
        serializer.save()
        # возвращаются данные из объекта
        return Response({'post': serializer.data})

    # удаление записи
    def delete(self, request, *args, **kwargs):
        # получает ключ записи
        pk = kwargs.get("pk", None)
        # проверяет ключ
        if not pk:
            return Response({"error": "Метод DELETE не определён"})

        # пробует удалить запись по ключу
        try:
            Women.objects.get(pk=pk).delete()
        except:
            return Response({"error": "Объект не найден"})

        # возвращаются данные которые были удалены
        return Response({'post': "удалена строка " + str(pk)})


# класс не подключён
# оставлен на память: отображение списка модели
class WomenAPIViewList(generics.ListAPIView):
    queryset = Women.objects.all()  # считывание всех данных из модели
    serializer_class = WomenSerializer  # назначение сериализатора
