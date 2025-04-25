import django_filters
from .models import Product,category,Brands




class ProductFilter(django_filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    category_product = django_filters.ModelMultipleChoiceFilter(
        queryset=category.objects.all()
    )

    brand = django_filters.ModelChoiceFilter(
        queryset=Brands.objects.all()
    )
    class Meta:
        model = Product
        fields = ['price_min', 'price_max', 'name', 'category_product', 'brand']