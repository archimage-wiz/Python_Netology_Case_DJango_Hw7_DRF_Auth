from django.contrib.auth.models import User
from django_filters import FilterSet, DateFromToRangeFilter
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, PermissionDenied

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""
    username = serializers.CharField(allow_blank=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        read_only_fields = ['id', ]


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""
    creator = UserSerializer(read_only=True)
    title = serializers.CharField(allow_blank=False)
    description = serializers.CharField(max_length=1024)

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator', 'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # if instance.creator != self.context["request"].user:
        #     raise PermissionDenied('error, not an owner')
        return super().update(instance, validated_data)

    def validate(self, data):
        if data.get('status') and data.get('status') == 'open':
            if Advertisement.objects.filter(
                    creator=self.context['request'].user,
                    status=AdvertisementStatusChoices.OPEN).count() >= 10:
                raise ValidationError('error, more than 10 advertisements')
        return data


