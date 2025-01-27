from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    movie_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id name movie_count').split()

    def get_movie_count(self, directors):
        return directors.movie.count()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id text movie stars').split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    review = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director review rating'.split()

    def get_rating(self, movie):
        reviews = movie.review.all()
        if reviews:
            sum_reviews = sum([review.stars for review in reviews])
            average = sum_reviews / len(reviews)
            return average
        return None


class MovieValidSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()
    director = serializers.IntegerField()


class ReviewValidSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie = serializers.IntegerField()
    stars = serializers.IntegerField(min_value=1,max_value=5)
