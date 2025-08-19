from django.urls import path
from . import views  # Importação relativa das views do app genres


urlpatterns = [ 
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),  # Include the genres app URLs
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),  # Detail view for a specific genre
]