from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField
from rest_framework.validators import UniqueValidator



class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password',
                  'first_name', 'last_name', 'date_joined')
        extra_kwargs = {'email': {'allow_blank': False, 'required': True, 'validators': [
            UniqueValidator(queryset=User.objects.all())]},'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj
