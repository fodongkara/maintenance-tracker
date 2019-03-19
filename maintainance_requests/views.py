from django.shortcuts import render
from maintainance_requests.models import MaintainanceRequest
from maintainance_requests.serializers import MaintainanceRequestSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

class MaintainanceRequestViewSet(ModelViewSet):
    """API Endpoint for viewing and editting user details"""
    queryset = MaintainanceRequest.objects.all().order_by('-date_posted')
    serializer_class = MaintainanceRequestSerializer

    filter_backends = (SearchFilter,)
    search_fields = ('request_title', 'request_description', 'author__username')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.is_superuser and "status" in self.request.data:
            serializer.save()
        elif "status" in self.request.data:
            return Response({'Message': 'You have successfully register'})
        elif not self.request.user.is_superuser:
            serializer.save(author=self.request.user)
        
    def list(self, request):
        if request.user.is_superuser:
            permission_classes = (IsAdminUser,)
            queryset = MaintainanceRequest.objects.all()
            serializer = MaintainanceRequestSerializer(queryset, many=True,context={'request': request})
            return Response(serializer.data)
        return Response('Un Authorised, you need admin rights')
