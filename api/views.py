from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
import uuid
from .helpers import GameEngine
from .models import Ship, Position
from .serializers import ShipSerializer

logger = logging.getLogger('django')
ge = GameEngine(10,1,2,3,4)

@api_view(['GET'])
def generate_party(request):
    logger.info("Generate a new party !!")
    return Response(
        {
            'uuid': ge.create_game_board()
        }
    )

@api_view(['GET'])
def get_party(request, uuid):
    logger.info("Get party number : "+uuid)
    return Response(ge.get_game(uuid))

@api_view(['PUT'])
def update_ship(request, pk):
    try:
        ship = Ship.objects.get(pk=pk)
    except Ship.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ShipSerializer(ship, data=request.data['ship'])
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_position(request, pk):
    try:
        position = Position.objects.get(pk=pk)
    except Position.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ShipSerializer(position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)