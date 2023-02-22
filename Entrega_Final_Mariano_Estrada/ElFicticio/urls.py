from django.urls import path
from ElFicticio.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', v_inicio, name="Inicial"),
    path("notas/", v_notas, name="Publicaciones"),
    path("editor/", v_editor, name="Editorial"),
    path("contacto/",v_contacto, name="Contactanos"),
    path("login/",v_inicioSesion,name="Login"),
    path("registro/",v_registro,name="Registro"),    
    path("logout",LogoutView.as_view(template_name="ElFicticio/logout.html"),name="Logout"),
    path("editar/",v_editar,name="Editar"),
]
