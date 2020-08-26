from comment.models import Aspect
import random

def generate_fake_data():
    aspect_polarity=["positive","negative","neutral"]
    aspect_category=["AMBIENCE#GENERAL","DRINKS#PRICES","DRINKS#QUALITY","DRINKS#STYLE_OPTIONS","FOOD#PRICES","FOOD#QUALITY","FOOD#STYLE_OPTIONS","LOCATIOn#GENERAL","RESTAURANT#GENERAL","RESTAURANT#MISCELLANEOUS","SERVICE#GENERAL"]
    
    all_aspect=Aspect.objects.all()
    for aspect in all_aspect:
        aspect.category=random.choice(aspect_category)
        aspect.polarity=random.choice(aspect_polarity)
        aspect.save()