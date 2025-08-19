from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from datetime import date


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        # reviews = obj.reviews.all()
        # if reviews.exists():
        #     total_rate = sum(review.stars for review in reviews)
        #     return round(total_rate / reviews.count(), 1)
        # return None
    
    
    def validate_release_date(self, value):
        if value.year > date.today().year:
            raise serializers.ValidationError("A data de lançamento do Filme não pode ser maior que a data atual!")
        return value

    def validate(self, attrs):
        if attrs['resume'] == '':
            raise serializers.ValidationError("O campo Resumo não pode ser vazio!")
        return attrs