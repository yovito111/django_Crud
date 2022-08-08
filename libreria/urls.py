from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos, name='productos'),
    path('productos/crear', views.crear_producto, name='crear' ),
    path('productos/editar', views.editar, name='editar' ),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('productos/editar/<int:id>', views.editar, name='editar'),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)