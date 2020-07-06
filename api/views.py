from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging
import uuid

logger = logging.getLogger(__name__)

@api_view(['GET'])
def generate_party(request):
    logger.debug("Generate a new party !!")
    return Response(
        {
            'test_value': test,
            'uuid': str(uuid.uuid4())
        }
    )
