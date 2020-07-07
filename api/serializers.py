from rest_framework.serializers import ModelSerializer
from .models import Party, Grid, Position, Ship, ShipType

class PartySerializer(ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'

class GridSerializer(ModelSerializer):
    class Meta:
        model = Grid
        fields = '__all__'

class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class ShipSerializer(ModelSerializer):
    class Meta:
        model = Ship
        fields = '__all__'

class ShipTypeSerializer(ModelSerializer):
    class Meta:
        model = ShipType
        fields = '__all__'