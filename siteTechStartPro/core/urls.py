from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('detalhe-produto/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('novo-produto', views.ProductCreate.as_view(), name='product_create'),
    path('editar-produto/<int:pk>', views.ProductUpdate.as_view(), name='product_update'),
    path('excluir-produto/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
]
