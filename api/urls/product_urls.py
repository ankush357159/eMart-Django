from django.urls import path
from api.views.category_views import CategoryDeleteView, CategoryDetailsView, CategoryListView, CategoryUpdateView, CreateCategoryView

from api.views.product_views import CreateProductView, ProductDeleteView, ProductDetailsView, ProductImageUploadView, ProductListView, ProductUpdateView, ProductReviewCreateView

from api.views import product_views


urlpatterns = [
    path('create_product/', CreateProductView.as_view(), name='create_product'),
    path('upload_image/', product_views.uploadImage, name='upload'),
    path('products/', ProductListView.as_view(), name='list_products'),
    path('product_details/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('<str:pk>/reviews/', ProductReviewCreateView.as_view(), name='create_review'),



    path('create_category/', CreateCategoryView.as_view(), name='create_category'),
    path('categories/', CategoryListView.as_view(), name='list_categories'),
    path('category_details/<int:pk>/', CategoryDetailsView.as_view(), name='category_details'),
    path('update_category/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),
]