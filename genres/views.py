from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from genres.models import Genre
from genres.serializers import GenreModelSerializer


# Create your views here.
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission,]  # Ensure the user is authenticated to access this view
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaultPermission,]  # Ensure the user is authenticated to access this view
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))  # Transoforma o conteúdo JSON em um dicionário
#         genre = Genre(name=data['name'])
#         genre.save()
#         return JsonResponse({'id': genre.id, 'name': genre.name}, status=201)


# @csrf_exempt
# def genre_detail_view(request, pk):
#     genre = get_object_or_404(Genre,pk=pk)
    
#     if request.method == 'GET':
#         data = {'id': genre.id, 'name': genre.name}
#         return JsonResponse(data)
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))  # Transoforma o conteúdo JSON em um dicionário
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse({'id': genre.id, 'name': genre.name})
#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse({'message': 'Gênero excluído com sucesso.'}, status=204, )