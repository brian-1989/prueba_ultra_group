from rest_framework import serializers

class CreateNewHotelSerializer(serializers.Serializer):
    city_name = serializers.CharField(allow_blank=False, required=True, max_length=100)
    hotel_name = serializers.CharField(allow_blank=False, required=True, max_length=100)

class UpdateHotelSerializer(serializers.Serializer):
    hotel_name = serializers.CharField(allow_blank=False, required=True, max_length=100)
    field = serializers.CharField(allow_blank=False, required=True, max_length=100)
    value = serializers.CharField(allow_blank=True, required=False, max_length=100)

class DeleteHotelSerializer(serializers.Serializer):
    hotel_name = serializers.CharField(allow_blank=False, required=True, max_length=100)