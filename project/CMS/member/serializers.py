from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.Serializer):
    userid = serializers.CharField()
    password = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = Member
        fields = '__all__'

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Member.objects.filter(pk=instance.userid).update(**validated_data)
        return Member

