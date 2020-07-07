from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
import uuid
from .helpers import GameEngine

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