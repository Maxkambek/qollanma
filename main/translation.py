from modeltranslation.translator import register, TranslationOptions
from .models import Useful, Offer, News


@register(Useful)
class UsefulTrans(TranslationOptions):
    fields = ['title', 'content']


@register(Offer)
class OfferTrans(TranslationOptions):
    fields = ['name', 'subtitle', 'date']


@register(News)
class NewsTrans(TranslationOptions):
    fields = ['title', 'content']
