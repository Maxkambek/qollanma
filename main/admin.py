from django.contrib.admin import register, ModelAdmin
from .models import Useful, Offer, Contact, Feedback, News
from modeltranslation.admin import TranslationAdmin


@register(Useful)
class UsefulAdmin(TranslationAdmin):
    list_display = ['title', 'id']


@register(Offer)
class OfferAdmin(TranslationAdmin):
    list_display = ['name', 'date', 'price', 'id']


@register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'id']


@register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ['name', 'phone']


@register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = ['id', 'message']
