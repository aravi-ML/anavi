import dateparser
from re import findall,sub
from lxml import html
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pprint import pprint
from xvfbwrapper import Xvfb

from hotel.model.hotel import Hotel
from hotel.hotel_service import HotelService
from website.model.website import WebSite
from website.website_service import WebSiteService
from hotel.model.hotel_website import HotelWebSite
from hotel.hotel_website_service import HotelWebSiteService
from comment.model.comment import Comment
from comment.comment_service import CommentService
from .google_pre_links import links_hotel
import datetime

class GoogleTravelCrawler:
    name="google travel"
    url="https://www.google.com/travel/hotels"
    website=None
    def add_website(self):
        nweb=WebSite()
        nweb.name=self.name
        nweb.link=self.url
        wservice=WebSiteService()
        response=wservice.add(nweb)
        self.website=response["website"]
        return self.website
    
    def parse(self):
        self.add_website()
        driver=webdriver.Firefox()
        driver.get(self.url)
        sleep(25)
        #search_input=driver.find_element_by_id("oA4zhb")
        search_input=driver.find_elements_by_css_selector(".whsOnd.zHQkBf")[1]
        search_input.send_keys("Cameroon")
        search_input.send_keys(Keys.ENTER)
        sleep(10)
        #on defnis les elements qui vont entrez dans les hotels que nous allons parcourir
        links_hotel=[]
        names_hotel=[]
        #une liste de nom et une liste lien

        total_hotel=driver.find_element_by_id("wKdiD").text
        nb_iteration=14
        time_to_wait=6
        while nb_iteration>0:
            list_hotel=driver.find_elements_by_css_selector(".uaTTDe.BcKagd.Ab08je.mlo5Vd")
            for item_hotel in list_hotel:
                link=""
                try:   
                    link=item_hotel.find_element_by_css_selector(".spNMC.lRagtb").get_attribute("href")
                except:
                    pass
                links_hotel.append(link)
                try:
                    next_btn=driver.find_element_by_css_selector(".U26fgb.O0WRkf.oG5Srb.C0oVfc.JDnCLc.yHhO4c.yNl8hd.zbLWdb")
                    next_btn.click()
                    sleep(time_to_wait)
                except:
                    nb_iteration=0
            nb_iteration=nb_iteration-1
        #Maintenant nous allons suivre les liens que nous avons sauvegarder plutot
        hservice=HotelService()
        cservice=CommentService() #on definit celui avec qui on va ajouter les commentaire
        print("Le nombre d'hotel est "+str(len(links_hotel)))
        for link_item in links_hotel:
            #print("Entrer dans for")
            if(link_item!=""):
                try:
                    #print("Weclome to my first hotel")
                    driver.get(link_item)
                    sleep(10)
                    nhotel=Hotel()
                    nhotel.name=driver.title
                    nhotel.place="Cameroon"
                    hotel_add=hservice.add_hotel(nhotel)
                    nhotel=hotel_add["hotel"]

                    #maintenant nous devons associers a un siteweb
                    hwebsite=HotelWebSite()
                    hwservice=HotelWebSiteService()
                    hwebsite.hotel=nhotel
                    hwebsite.website=self.website
                    hwservice.add(hwebsite)

                    #maintenant que c'est ajouter nous devons recuperer les commentaires
                    #mais avant faisons d'abord un scrool infernal
                    scroll_number=33
                    scroll_wait_time=3
                    html=driver.find_element_by_tag_name("html")
                    while scroll_number>0:
                        html.send_keys(Keys.PAGE_DOWN)
                        html.send_keys(Keys.PAGE_DOWN)
                        html.send_keys(Keys.PAGE_DOWN)
                        scroll_number=scroll_number-1
                        sleep(scroll_wait_time)
                    #maintenant on va recuper
                    all_reviews_card=driver.find_elements_by_css_selector(".Svr5cf.bKhjM")
                    for card_item in all_reviews_card:
                        comment=Comment()
                        comment.text=card_item.find_element_by_css_selector(".kVathc .STQFb .K7oBsc div span").text
                        comment.hotel=nhotel
                        comment.website=self.website
                        date_comment=card_item.find_element_by_css_selector(".iUtr1").text
                        date_comment=date_comment.split(" on ")[0]
                        try:
                            comment.add_date=dateparser.parse(date_comment)
                            cservice.add(comment)
                        except:
                            comment.add_date=datetime.datetime.now()
                            cservice.add(comment)
                except:
                    print("error i don't like")
        response={"links":links_hotel,"names":names_hotel,"website":self.website,"driver":driver}
        return response

    def parse_specific_links(self,links_hotel):
        self.add_website()
        hservice=HotelService()
        cservice=CommentService() #on definit celui avec qui on va ajouter les commentaire
        names_hotel=[]
        driver=webdriver.Firefox()
        print("Le nombre d'hotel est "+str(len(links_hotel)))
        for link_item in links_hotel:
            #print("Entrer dans for")
            if(link_item!=""):
                try:
                    #print("Weclome to my first hotel")
                    driver.get(link_item)
                    sleep(10)
                    nhotel=Hotel()
                    nhotel.name=driver.title
                    nhotel.place="Cameroon"
                    hotel_add=hservice.add_hotel(nhotel)
                    nhotel=hotel_add["hotel"]

                    #maintenant nous devons associers a un siteweb
                    hwebsite=HotelWebSite()
                    hwservice=HotelWebSiteService()
                    hwebsite.hotel=nhotel
                    hwebsite.website=self.website
                    hwservice.add(hwebsite)

                    #maintenant que c'est ajouter nous devons recuperer les commentaires
                    #mais avant faisons d'abord un scrool infernal
                    scroll_number=33
                    scroll_wait_time=3
                    html=driver.find_element_by_tag_name("html")
                    while scroll_number>0:
                        html.send_keys(Keys.PAGE_DOWN)
                        html.send_keys(Keys.PAGE_DOWN)
                        html.send_keys(Keys.PAGE_DOWN)
                        scroll_number=scroll_number-1
                        sleep(scroll_wait_time)
                    #maintenant on va recuper
                    all_reviews_card=driver.find_elements_by_css_selector(".Svr5cf.bKhjM")
                    for card_item in all_reviews_card:
                        comment=Comment()
                        comment.text=card_item.find_element_by_css_selector(".kVathc .STQFb .K7oBsc div span").text
                        comment.hotel=nhotel
                        comment.website=self.website
                        date_comment=card_item.find_element_by_css_selector(".iUtr1").text
                        date_comment=date_comment.split(" on ")[0]
                        try:
                            comment.add_date=dateparser.parse(date_comment)
                            cservice.add(comment)
                        except:
                            comment.add_date=datetime.datetime.now()
                            cservice.add(comment)
                except:
                    print("error i don't like")
        response={"links":links_hotel,"names":names_hotel,"website":self.website,"driver":driver}
        return response  
            
