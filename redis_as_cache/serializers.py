
from rest_framework.serializers import ModelSerializer
from django.apps import apps
CountryModel = apps.get_model("redis_as_cache", "Country")
"""
The serializer below is the same as this serializer

class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=56)
    population = serializers.IntegerField()
    image = serializers.TextField()

    def create(self, validated_data):
        return Country.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.population = validated_data.get(
            'population', instance.population)
        image = validated_data.get('image', instance.image)
        instance.save()
        return instance
"""


class CountrySerializer(ModelSerializer):
    class Meta:
        model = CountryModel
        fields = ['name', 'population', 'image']


class CountrySerializerFetcher:
    def get_country_serializer(self, data):
        return CountrySerializer(data=data)
