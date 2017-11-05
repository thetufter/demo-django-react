from rest_framework import serializers
from .models import Person


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'email')
