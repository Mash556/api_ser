from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # добавляет все поля из Product
        # exclude = [] за исключение

    # def validate_title(self, value):
    #     if len(value) > 50:
    #         raise serializers.ValidationError('title length more than 50')
    #     return value
    
    def validate(self, attrs):
        return super().validate(attrs)