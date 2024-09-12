from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта, позволяющее редактировать его только владельцам объекта.
    Предполагается, что экземпляр модели имеет атрибут «владелец».
    """

    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение разрешены для любого запроса,
        # поэтому мы всегда разрешаем запросы GET, HEAD или OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Экземпляр должен иметь атрибут с именем «владельца».
        return obj.user == request.user
