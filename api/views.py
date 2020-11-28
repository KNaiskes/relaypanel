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


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def relay(request, pk):
    try:
        relay = Relay.objects.get(pk=pk)
    except Relay.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if relay.owner != request.user:
        return Response({'response': 'You do not have permissions for this action'})

    if request.method == 'GET':
        serializer = RelaySerializer(relay, context={'request': request})
        return Response({'data': serializer.data})
    elif request.method == 'PUT':
        serializer = RelaySerializer(relay, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        relay.delete()
        return  Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def new_relay(request):
    if request.method == 'POST':
        owner = Relay(owner=request.user)
        serializer = RelaySerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
