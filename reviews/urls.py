from django.urls import path
from . import views  # Importação relativa das views do app reviews

urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='review-create-list'),  # Include the movies app URLs
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),  # Detail view for a specific movie
]