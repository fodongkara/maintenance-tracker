from django.shortcuts import render
from maintainance_requests.models import MaintainanceRequest
from maintainance_requests.serializers import MaintainanceRequestSerializer 
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

class MaintainanceRequestViewSet(ModelViewSet):
    """API Endpoint for viewing and editting user details"""
    queryset = MaintainanceRequest.objects.all().order_by('-date_posted')
    serializer_class = MaintainanceRequestSerializer

    filter_backends = (SearchFilter,)
    search_fields = ('request_title', 'request_description', 'author__username')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
