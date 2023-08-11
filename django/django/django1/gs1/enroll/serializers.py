from dataclasses import fields
from rest_framework import serializers
from enroll.models import enroll

class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=enroll
        fields=(id,'name','capital')