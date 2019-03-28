from django.shortcuts import render
from maintainance_requests.models import MaintainanceRequest
from maintainance_requests.serializers import MaintainanceRequestSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from django.http import JsonResponse
import logging

class MaintainanceRequestViewSet(ModelViewSet):
    """API Endpoint for viewing and editting user details"""
    queryset = MaintainanceRequest.objects.all().order_by('-date_posted')
    serializer_class = MaintainanceRequestSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    filter_fields = ('request_title', 'request_description','status')
    search_fields = ('request_title', 'request_description', 'author__username', 'status')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.is_superuser and "status" in self.request.data:
            serializer.save()
        elif "status" in self.request.data:
            return Response({'Message': 'You have no rights to change status'})
        elif not self.request.user.is_superuser:
            serializer.save()
        
    def list(self, request):
        status = self.request.query_params.get('status') # List of ids
        if request.user.is_superuser:
            queryset = MaintainanceRequest.objects.all()
            if status:
                queryset = MaintainanceRequest.objects.all().filter(status=status) 
        else:
            user = request.user
            queryset = MaintainanceRequest.objects.all().filter(author=user)
            if status:
                queryset = MaintainanceRequest.objects.all().filter(author=user,status=status)
        serializer = MaintainanceRequestSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)