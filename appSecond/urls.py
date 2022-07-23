from django.urls import include, path
from rest_framework import routers
from appSecond import views

app_name = "appSecond"

router = routers.DefaultRouter()

urlpatterns = [
                    path('cliente', views.clienteLista.as_view(), name="cliente-lista"),
                    path('cliente/<int:pk>', views.clienteDetalle.as_view(), name="cliente-detalle"),
                    path('mesa', views.mesaLista.as_view(), name="mesa-lista"),
                    path('mesa/<int:pk>', views.mesaDetalle.as_view(), name="mesa-detalle"),
                    path('pedido', views.pedidoLista.as_view(), name="pedido-lista"),
                    path('pedido/<int:pk>', views.pedidoDetalle.as_view(), name="pedido-detalle"),
                    path('platillo', views.platilloLista.as_view(), name="platillo-lista"),
                    path('platillo/<int:pk>', views.platilloDetalle.as_view(), name="platillo-detalle"),
                    path('mesero', views.meseroLista.as_view(), name="mesero-lista"),
                    path('mesero/<int:pk>', views.meseroDetalle.as_view(), name="mesero-detalle"),
                    path('factura', views.facturaLista.as_view(), name="factura-lista"),
                    path('factura/<int:pk>', views.facturaDetalle.as_view(), name="factura-detalle"),
                ]

