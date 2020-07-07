from rest_framework import serializers
from .models import Party, Grid, Position, Ship, ShipType

class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class ShipSerializer(serializers.ModelSerializer):
    party = serializers.PrimaryKeyRelatedField(read_only=True)
    ship_type = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Ship
        fields = '__all__'

class ShipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipType
        fields = '__all__'