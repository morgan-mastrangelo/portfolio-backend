from .models import CommentModel
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'