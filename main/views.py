from rest_framework import generics
from .models import Useful, Offer, Contact, Feedback, News
from .serializers import UsefulSerializer, ContactSerializer, FeedbackSerializer, OfferSerializer, NewsSerializer


class UsefulListAPIView(generics.ListAPIView):
    queryset = Useful.objects.all()
    serializer_class = UsefulSerializer


class OfferListAPIView(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class FeedbackAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
