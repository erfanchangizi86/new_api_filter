# products/urls.py

from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import ProductGenericView,ProductDetailView
from products.views import CategoryDetailView,BrandGenericView,CategoryGenericView,BrandDetailView

# router = DefaultRouter()
# router.register(r'product',ProductViewSet , basename='user')
# urlpatterns = router.urls

urlpatterns = [
    path('products/', ProductGenericView.as_view(), name='product'),
    path('product/<slug>', ProductDetailView.as_view(), name='details'),
    path('categorys/',CategoryGenericView.as_view(), name='category'),
    path('category/<pk>', CategoryDetailView.as_view(), name='categoryDetails'),
    path('Brands/', BrandGenericView.as_view(), name='Brands'),
    path('Brand/<pk>', BrandDetailView.as_view(), name='brand'),
]
