from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'publisher')
        
class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfume
        fields = ('id', 'name', 'brand', 'price')        