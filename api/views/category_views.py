from api.models import Category
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics

from api.serializers.productSerializers import CategorySerializer


# Create Category - Admin
class CreateCategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated,]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = CategorySerializer

# List All Categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = CategorySerializer


# Get Category Details
class CategoryDetailsView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = CategorySerializer


# Update Category - (PUT & PATCH) - Admin
class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated,]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = CategorySerializer
    

# Delete Category - Admin
class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = CategorySerializer




    