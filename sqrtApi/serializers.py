from rest_framework import serializers
from sqrtApi.models import SqrtNumber


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = SqrtNumber
        fields = ('number','sqrt',)