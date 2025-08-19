from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from actors.models import Actor
from actors.serializers import ActorModelSerializer

# Create your views here.
class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission,]  # Ensure the user is authenticated to access this view
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission,]  # Ensure the user is authenticated to access this view
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
