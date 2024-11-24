from rest_framework import serializers
from E_Book_App.reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
