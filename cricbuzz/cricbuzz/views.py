from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Data, Subscription
from .serializers import DataSerializer, SubscriptionSerializer


class FeaturedList(APIView):
    """
    List all the records if their is_featured flag is TRUE
    """

    def get(self, request, format=None):
        data_qs = Data.objects.filter(is_featured=True)
        serializer = DataSerializer(data_qs, many=True)
        return Response(serializer.data)


class VideosList(APIView):
    """
    List all the records if their is_video flag is TRUE
    """

    def get(self, request):
        data_qs = Data.objects.filter(is_video=True)
        serializer = DataSerializer(data_qs, many=True)
        return Response(serializer.data)


class EditorialList(APIView):
    """
    List all the records if their is_video flag is FALSE
    """

    def get(self, request):
        data_qs = Data.objects.filter(is_video=False)
        serializer = DataSerializer(data_qs, many=True)
        return Response(serializer.data)


class SubscriptionList(APIView):
    """
    List all the subscription plans
    """

    def get(self, request):
        subscription_qs = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription_qs, many=True)
        return Response(serializer.data)
