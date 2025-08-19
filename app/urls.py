from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),  # Include the authentication app URLs
    path('api/v1/', include('genres.urls')),  # Include the genres app URLs
    path('api/v1/', include('actors.urls')),  # Include the actors app URLs
    path('api/v1/', include('movies.urls')),  # Include the movies app URLs
    path('api/v1/', include('reviews.urls')),  # Include the reviews app URLs
]
