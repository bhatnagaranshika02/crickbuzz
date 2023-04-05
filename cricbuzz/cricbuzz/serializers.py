from rest_framework import serializers
from .models import Data, Subscription

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['title', 'url', 'thumbnail', 'description', 'is_video', 'is_premium', 'is_featured']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['title', 'url', 'description', 'features', 'price']
