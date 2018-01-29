from rest_framework import serializers
from .models import Dog, Cat


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = ('name', 'bday')



class CatSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cat
		fields = ('name', 'bday')

