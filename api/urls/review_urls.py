from django.urls import path
from api.views.review_views import CreateReviewView, ReviewListView, ReviewDetailsView, ReviewDeleteView


urlpatterns = [
    path('create_review/', CreateReviewView.as_view(), name='create_review'),
    path('reviews/', ReviewListView.as_view(), name='list_reviews'),
    path('review_details/<int:pk>/', ReviewDetailsView.as_view(), name='review_details'),
    path('delete_review/<int:pk>/', ReviewDeleteView.as_view(), name='delete_review'),
]