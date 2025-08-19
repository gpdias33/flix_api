from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Avaliação não pode ser menor que 1'),
            MaxValueValidator(5, 'Avaliação não pode ser maior que 5'),
        ]
        )
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.movie.title} - {self.stars} stars'