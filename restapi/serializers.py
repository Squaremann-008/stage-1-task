from rest_framework import serializers
from .models import Input, student

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['slackUsername', 'backend', 'age', 'bio']

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ['operation_type', 'x', 'y']