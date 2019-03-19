from maintainance_requests.models import MaintainanceRequest
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault, ValidationError
from rest_framework import serializers


class MaintainanceRequestSerializer(HyperlinkedModelSerializer):
    author = PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    status = 'pending'

    def validate_status(self, status):
        if status not in ["pending", "approved", "rejected"]:
            raise ValidationError(
                "status should be pending,approved or rejected")
        return status

    class Meta:
        model = MaintainanceRequest
        fields = ('url', 'request_title', 'request_description',
                  'date_posted', 'author', 'comment', 'status')
