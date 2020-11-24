#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Relay
from .serializers import RelaySerializer

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def relays(request):
    if request.method == 'GET':
        relays_list = Relay.objects.filter(owner=request.user)
        serializer = RelaySerializer(relays_list,
                        context={'request': request}, many=True)

        return Response({'relays': serializer.data})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def relay(request, pk):
    try:
        relay = Relay.objects.get(pk=pk)
    except Relay.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RelaySerializer(relay, context={'request': request})
        return Response({'data': serializer.data})
