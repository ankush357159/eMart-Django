from api.models import Review
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics

from api.serializers.productSerializers import ReviewSerializer


# Create Review 
class CreateReviewView(generics.CreateAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated,]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ReviewSerializer
    

# List All Reviews
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = ReviewSerializer


# Get Review Details
class ReviewDetailsView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = ReviewSerializer


# Delete Review - Admin
class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ReviewSerializer




    