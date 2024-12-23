from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IPO
from .serializers import IPOSerializer

class IPOList(APIView):
    def get(self, request):
        ipo_data = IPO.objects.all()
        serializer = IPOSerializer(ipo_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class IPODetail(APIView):
    def get(self, request, pk):
        try:
            ipo = IPO.objects.get(pk=pk)
        except IPO.DoesNotExist:
            return Response({'error': 'IPO not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IPOSerializer(ipo)
        return Response(serializer.data, status=status.HTTP_200_OK)
