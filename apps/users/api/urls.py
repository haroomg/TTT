from django.urls import path
from apps.users.api.api import UserApiView

urlpatterns = [
    path("usuario/", UserApiView.as_view(), name="usuario_api")
]
