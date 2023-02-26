from rest_framework import serializers
from database.models import *

class question_serialisers(serializers.ModelSerializer):
    class Meta:
        model = teacher
        fields = '__all__'  




