from api.models import Product, Review
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework import status

from api.serializers.productSerializers import ProductSerializer


# Create Product - Admin
class CreateProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProductSerializer

# List All Products
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = ProductSerializer


# Get Product Details
class ProductDetailsView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = ProductSerializer


# Update Product - (PUT & PATCH) - Admin
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated,]
    # parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProductSerializer
    

# Delete Product - Admin
class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ProductSerializer


#Upload Image
class ProductImageUploadView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ProductSerializer
    lookup_field = 'pk'
  

@api_view(['POST'])
def uploadImage(request):
        data = request.data
        productId = data['productId']
        product = Product.objects.get(id=productId)
        product.image = request.FILES.get('image')
        product.save()
        return Response()



class ProductReviewCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ProductSerializer

    def create(self, request, pk, *args, **kwargs):
        user = request.user
        product = Product.objects.get(id=pk)
        data = request.data

        # Check review already exists
        alreadyExists = product.review.filter(user=user).exists()

        if alreadyExists:
            content = {'detail': 'Product already reviewed'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        # No rating or 0
        elif data['ratings'] == 0:
            content = {'detail': 'Please select a rating'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        else:
            review = Review.objects.create(
                user = user,
                product = product,
                name = user.first_name,
                rating = data['ratings'],
                comment = data['comment'],
            )

            reviews = product.review.all()
            product.numReviews = len(reviews)

            total = 0

            for i in reviews:
                total += i.rating
            product.rating = total/len(reviews)
            product.save()

            return Response('Review Added')