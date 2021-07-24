from rest_framework import serializers
from .models import appt

class apptSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=appt
        fields='__all__'