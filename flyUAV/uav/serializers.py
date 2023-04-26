from rest_framework import serializers

from rest_framework import serializers
from .models import Model,Brand,Category,ihaModel
from django.contrib.auth import authenticate




class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=Brand
        fields=('name','id',)

    def create(self, validated_data):
        """
        Create and return a new Snippet instance, given the validated data.
        """
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Snippet instance, given the validated data.
        """
        instance.brand_name = validated_data.get('name', instance.title)
        instance.save()
        return instance

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Model
        fields=('name','id',)

    def create(self, validated_data):
        """
        Create and return a new Snippet instance, given the validated data.
        """
        return Model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Snippet instance, given the validated data.
        """
        instance.brand = validated_data.get('brand', instance.model_brand)
        instance.name = validated_data.get('name', instance.model_name)
        instance.save()
        return instance

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('name','id',)

class IhaSerializerPost(serializers.ModelSerializer):

    class Meta:
        model=ihaModel
        fields=('brand','model','weight','category','image','id','date',)

class IhaSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model=ihaModel
        fields=('brand','model','weight','category','image','id',)
class IhaSerializerGet(serializers.ModelSerializer):
    brand=BrandSerializer()
    model=ModelSerializer()
    category=CategorySerializer()
    class Meta:
        model=ihaModel
        fields=('brand','model','weight','category','image','id',)