# Django import
from django.contrib.auth.models import User

# Rest Framework import
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


# Local Import
from api.serializers.userSerializers import ChangePasswordSerializer, RegisterUserSerializer

   
# Create New User
class RegisterUserCreatView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterUserSerializer


# Get User Details
class RegisterUserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterUserSerializer


# Update User Details PUT & PATCH
class RegisterUserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = RegisterUserSerializer


# Delete User
class RegisterUserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = RegisterUserSerializer


# List All Users
class RegisterUserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = RegisterUserSerializer


# Change Password
class ChangePasswordView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = ChangePasswordSerializer


# User Details
class UserDetailsView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = RegisterUserSerializer
    def get(self, request):
        user_name = request.user
        print(user_name)

