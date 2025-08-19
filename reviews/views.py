from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from reviews.models import Review
from reviews.serializers import ReviewModelSerializer   

# Create your views here.
class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission,]  # Ensure the user is authenticated to access this view
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission,]  # Ensure the user is authenticated to access this view
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer