from django.urls import path
from . import views

urlpatterns = [
    path('useful/', views.UsefulListAPIView.as_view()),
    path('news/', views.NewsListAPIView.as_view()),
    path('offers/', views.OfferListAPIView.as_view()),
    path('contact/', views.ContactAPIView.as_view()),
    path('feedback/', views.FeedbackAPIView.as_view())
]
