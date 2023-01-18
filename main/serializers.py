from rest_framework import serializers
from .models import Useful, Offer, News, Feedback, Contact


class UsefulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useful
        fields = ['id', 'title', 'content']


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'name', 'subtitle', 'date', 'price', 'image', 'price_dollar']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'created_at', 'title', 'content', 'image']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone', 'message']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['message']
