from rest_framework import viewsets
from django.contrib.auth.models import User
from collection import models
from collection import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CollectionViewset(viewsets.ModelViewSet):

    """ Token based authentication"""
    # permission_classes = (IsAuthenticated,)

    queryset = models.Collection.objects.all()
    serializer_class = serializers.CollectionSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        # user_id = data.user_id
        # user = User.objects.filter(id=user_id)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response({"Success": "true"}, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
