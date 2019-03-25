from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField
from rest_framework.validators import UniqueValidator



class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password',
                  'first_name', 'last_name', 'date_joined')
        extra_kwargs = {
            'email': {
                'allow_blank': False,
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all())]
            },
            'password': {
                'write_only': True
            },
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            }
        }

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        user_obj = User(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user_obj.set_password(password)
        user_obj.save()
        return user_obj
