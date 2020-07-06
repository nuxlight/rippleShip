from django.shortcuts import render
from django.http import JsonResponse
import logging
import uuid

logger = logging.getLogger(__name__)

def generate_party(request):
    logger.debug("Generate a new party !!")
    return JsonResponse(
        {
            'uuid': str(uuid.uuid4())
        }
    )
