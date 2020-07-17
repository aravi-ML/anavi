from hotel.hotel_service import *
from comment.comment_service import *
from website.website_service import *


from .comment_audrey import *
from .commentaires_laure import *

def synchronize_booking():
    website=WebSite(name="Booking",link="https://www.bookings.com")
    website=WebSiteService().add(website)["website"]
    """Les cles sont les hotels et les valeurs sont une liste de commentaires"""
    for element in comments_audrey.keys():
        name=element.strip()
        hotels=Hotel.objects.filter(name__iexact=element.strip())
        print(hotels)
        hotel=Hotel()
        if(len(hotels)>0):
            hotel=Hotel(id=hotels[0].id)
        else:
            hotel=Hotel(name=name)
            hotel.save()
        
        #Nous allons parcourir chaque commentaire et l'ajouter
        current_comments=comments_audrey[element]
        for com_d in current_comments:
            for com in com_d[0]:
                com_t=com.strip()
                if(com_t!=""):
                    comment=Comment(text=com_t,website=website,hotel=hotel)
                    comment.save()


def synchronize_laure():
    pass