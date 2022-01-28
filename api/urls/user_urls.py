from django.urls import path

from api.views.user_views import RegisterUserCreatView, RegisterUserDetailView, RegisterUserUpdateView, RegisterUserDeleteView, RegisterUserListView, ChangePasswordView, UserDetailsView
from api.views.jwt_views import MyTokenObtainPairView, LogoutView

from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns=[
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login-fresh' ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register_user/', RegisterUserCreatView.as_view(), name='register_user'),
    path('user_details/', RegisterUserDetailView.as_view(), name='user_details'),
    path('profile_details/<int:pk>/', UserDetailsView.as_view(), name='user_details'),
    path('update_user/<int:pk>/', RegisterUserUpdateView.as_view(), name='update_user'),
    path('delete_user/<int:pk>/', RegisterUserDeleteView.as_view(), name='delete_user'),
    path('user_list/', RegisterUserListView.as_view(), name='user_list'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='change_password'),
]
