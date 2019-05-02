from collection.models import Collection
from rest_framework import serializers
from django.contrib.auth.models import User


class CollectionSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(write_only=True)

    class Meta:
        model = Collection
        fields = ('id', 'name', 'user_id')

    """Create with /collections and json: user_id=id and name=string """
    def create(self, validated_data):
        user_id = validated_data['user_id']
        user = User.objects.get(id=user_id)
        collect = Collection.objects.create(name=validated_data['name'], admin=user),
        return collect

    def get_queryset(self):
        queryset = {}
        param_user_id = self.request.query_params.get('user_id', None)
        if param_user_id is not None:
            queryset = Collection.objects.filter(admin__id=param_user_id)

        return queryset

