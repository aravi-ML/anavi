import demoji

from hotel.hotel_service import *
from comment.comment_service import *
from website.website_service import *


from .data.booking_comment import *
from .data.expedia_comments import *
import csv
import dateparser
import datetime
import random

def synchronize_booking():
    website=WebSite(name="Booking",link="https://www.bookings.com")
    website=WebSiteService().add(website)["website"]
    """Les cles sont les hotels et les valeurs sont une liste de commentaires"""
    for element in comments_audrey.keys():
        name=element.strip()
        hotels=Hotel.objects.filter(name__iexact=element.strip())
        hotel=Hotel()
        if(len(hotels)>0):
            hotel=Hotel(id=hotels[0].id)
        else:
            hotel=Hotel(name=name)
            hotel.save()
        
        #Nous allons parcourir chaque commentaire et l'ajouter
        current_comments=comments_audrey[element]
        print(element)
        i=0
        for com_d in current_comments:
            i+=1
            try:
                com_f=demoji.replace(com_d)
                comment=Comment(text=com_f,website=website,hotel=hotel)
                comment.save()
            except Exception as e:
                print(e)
                print(i)
            #comment.save()

def synchronize_expedia():
    website=WebSite(id=5)
    nb_hotel=len(Hotel.objects.all())
    comments_list=[]
    for com in expedia_comments:
        try:
            add_date=dateparser.parse(com["date"])
        except:
            add_date=datetime.datetime(2018,7,1,0,0,0)
        hotel=Hotel(id=random.randint(1,nb_hotel))
        comment=Comment(text=com["text"],add_date=add_date,website=website,hotel=hotel)
        comment.save()
        comments_list.append(comment)
    return comments_list

def syncronize_tripadvisor():
    date_to_english={"janvier":"january","février":"february","mars":"march","avril":"april","mai":"may","juin":"june","juillet":"july","août":"august","septembre":"september","octobre":"october","novembre":"november","décembre":"december"}

    website=WebSite(id=4)
    hotels_list=[]
    #On synchronize d'abord les hotels
    with open("data/dbexport/tripadvisor_hotel_list.csv") as hotel_file:
        data_hotel=csv.reader(hotel_file,delimiter=",")
        i=0
        for elt in data_hotel:
            if i>0:
                hotel=Hotel(name=elt[0],place="cameroun")
                hotel=HotelService().add_hotel(hotel)
                hotels_list.append(hotel)
            i=i+1
    #une fois finis on synchronise les commentaires
    hotel_number=len(Hotel.objects.all())
    comments_list=[]
    with open("data/dbexport/tripadvisor_comments.csv") as comment_file:
        data_comment=csv.reader(comment_file,delimiter=",")
        i=0
        for elt in data_comment:
            if(i>0):
                try:
                    str_date=elt[1].lower().strip()
                    str_date=str_date.split()
                    str_date=date_to_english[str_date[0]]+" "+str_date[1]
                    str_date=dateparser.parse(str_date)
                except:
                    str_date=datetime.datetime(2017,1,19,0,0,0)
                id_hotel=random.randint(1,hotel_number)
                comment=Comment(text=elt[0],add_date=str_date,hotel=Hotel(id=id_hotel),website=website)
                comment.save()
                comments_list.append(comment)
            i=i+1

    return hotels_list,comments_list
