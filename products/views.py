from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
from rest_framework.response import Response
from rest_framework.request import Request
from products.models import Product,category,Brands
from .Serializer import ProductSerializer,CategorySerializer,BrandSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .filters import ProductFilter
from django_filters.rest_framework import DjangoFilterBackend


def product_html(request):
    return render(request,'api_test/api.html')

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True, is_deleted=False)
    serializer_class = ProductSerializer


class ProductViewApi(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Product.objects.all()

    def get(self, request):
        products = self.get_queryset()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)\


class ProductDetail(APIView):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def  get(self,request,pk):
        return Response

    def put(self,request,pk):
        return Response
    def delete(self,request,pk):
        return Response


class  ProductGenericView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

# start category view
class  CategoryGenericView(ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
# end category view

class BrandGenericView(ListCreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer


class BrandDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'