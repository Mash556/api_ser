from rest_framework import serializers
from .models import Product

# serializers - он нам нужен чтобы ч питона в json перевести и наоборот

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' # добавляет все поля из Product
        # exclude = [] за исключение

    def validate_title(self, value):
        if len(value) > 50:
            raise serializers.ValidationError('title length more than 50')
        return value
    
    def validate(self, attrs):
        # self.validate_title(attrs['title'])
        return super().validate(attrs)
    

    