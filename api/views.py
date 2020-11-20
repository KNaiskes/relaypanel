#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Relay
from .serializers import RelaySerializer

@api_view(['GET'])
def relays(request):
    if request.method == 'GET':
        relays_list = Relay.objects.all()
        serializer = RelaySerializer(relays_list,
                        context={'request': request}, many=True)

        return Response({'relays': serializer.data})
