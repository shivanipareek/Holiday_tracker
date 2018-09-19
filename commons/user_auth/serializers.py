from django.contrib.auth.models import User
from rest_framework import serializers

from commons.user_auth.models import UserDetailInformation


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'first_name', 'last_name')


class UserDetailInformationSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserDetailInformation
        fields = ('last_login', 'last_notification_date',
        'language', 'user')
        read_only_fields = ('id',)



