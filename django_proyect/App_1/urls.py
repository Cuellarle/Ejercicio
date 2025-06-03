from django.urls import path
from . import views

#NOTAS
#Para iniciar el entorno virtual se debe dirigir al proyecto (django_proyect)
#Para iniciar el servidor es en terminal (cmd) con el pattern: python manage.py runserver
#Para migrar los modelos se introduce en terminal python manage.py makemigrations
#para confirmar la migracion de los modelos se esribe en cmd python manage.py migrate
#consola de python en cmd: python manage.py shell

urlpatterns = [
    path('', views.suma, name='suma'),
    path('muestras/<str:tipo_muestra>', views.muestras, name = "nombres_muestras"),
    path('pathview/<str:nombre>/<int:id>', views.pathview, name = "pathview_url"),
    path('getuser/', views.qryview, name = "qryview_url"),
    path("formularios/", views.muestra_formulario, name = "formularios_url"),
    path("getform/", views.getform, name = "getform_url"),
    path("datos/", views.datos_view, name = "datos_view_url"),
    path("registro/", views.logform, name = "registro_url"),
    
]