from django.urls import path
from . import views

# URLs for the movies app
urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movie-create-list'),  # Include the movies app URLs
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),  # Detail view for a specific movie
]