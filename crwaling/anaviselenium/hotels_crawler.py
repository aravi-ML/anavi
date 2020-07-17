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


class HotelsCrawler:
    """Cette classe est la pour cracker le site web hotels.com"""
    name="hotels"
    url="https://www.hotels.com"
    website=None
    def add_website(self):
        nweb=WebSite()
        nweb.name="hotels"
        nweb.link="https://www.hotels.com"
        wservice=WebSiteService()
        response=wservice.add(nweb)
        self.website=response["website"]
        return self.website

    def parse(self):
        self.add_website()

        #driver=webdriver.Chrome()
        driver=webdriver.Firefox()
        driver.get(self.url)
        sleep(20)
        search_input=driver.find_element_by_id("qf-0q-destination")
        search_input.send_keys("Cameroon") #maintenant que le cameroun a ete chosir
        sleep(7)
        random_element=driver.find_element_by_css_selector('h1')
        if random_element:
            random_element.click()
            sleep(10)
        
        #nav_list=driver.find_element_by_css_selector(".footer-nav-list")
        #nav_list.click()
        #envoyons des a present le boutton submit
        form_search=driver.find_element_by_css_selector("form.cont-bd") 
        #submit_button =driver.find_elements_by_css_selector("button[type='submit']")[0]
        clicked_per=False
        i_click=0
        submit_button =form_search.find_element_by_css_selector("button[type='submit']")
        submit_button.click()
        sleep(20)
        clicked_per=True
        i_click=i_click+1
        #Faisons le scroll pour charger le plus de commentaire possible
        i=0
        scroll_wait_time=6
        #last_height=driver.execute_script("return document.body.scrollHeight")
        html=driver.find_element_by_tag_name("html")
        while i<20:
            html.send_keys(Keys.PAGE_DOWN)
            html.send_keys(Keys.PAGE_DOWN)
            html.send_keys(Keys.PAGE_DOWN)
            html.send_keys(Keys.PAGE_DOWN)
            sleep(scroll_wait_time)
            i=i+1
        #fin de l'envoies des scroll
        
        #Maintenant nous devons avoir la liste des hotels qui ont ete charger 
        #list_hotel=driver.find_elements_by_css_selector("section.hotel-wrap")
        list_hotel=driver.find_elements_by_css_selector("li.hotel")
        final_hotel_list=[] #Cette liste va contenir tous les objets hotels obteu grace au scroll
        links_to_comment=[] #dans cette liste on va mettre les diffrents liens qui mene aux commentaire
        for hotel_item in list_hotel:
            #ici nous devons d'abord definis un hotel, ensuite verifier s'il est deja dans la base de donnes
            #Si il n'existe pas encore on l'ajoute sinon on recupere son identifiant
            #Ensuite on definirt une liaisons entre le site web et l'hotel
            #Si la liaisons n'existe pas on l'ajoute sinon on ne fait rien
            nhotel=Hotel()
            hotel_name=hotel_item.find_element_by_css_selector(".hotel-wrap .description .p-name").text
            hotel_web_id=hotel_item.get_attribute("data-hotel-id")
            hotel_place=hotel_item.find_element_by_css_selector(".hotel-wrap .description .contact .address").text

            nhotel.name=hotel_name
            nhotel.place=hotel_place
            nhotel.state=True

            hservice=HotelService()
            response={}
            exist=hservice.if_exist_hotel(nhotel)
            if(exist["status"]==False):
                response=hservice.add_hotel(nhotel)
                nhotel=response["hotel"]
            else:
                nhotel=exist["hotel"]
            
            hotelwebsite=HotelWebSite()
            hotelwebsite.hotel_id_in_website=hotel_web_id
            hotelwebsite.hotel=nhotel
            hotelwebsite.website=self.website
            #definition du lien entre un hotel et un site web
            hwservice=HotelWebSiteService()
            hwservice.add(hotelwebsite)
            #Maintenant que nous avons tout lancer, il est tant de recuperer les liens qui
            #menent aux commentaire il se peut que cela genere des erreurs pour lien non existant
            link=""
            try:
                link=hotel_item.find_element_by_css_selector(".reviews-box .guest-reviews-link").get_attribute("href")
            except:
                pass
            links_to_comment.append(link)
            final_hotel_list.append(nhotel)
        #maintenant nous allons suivre les liens lies au commentaire
        i=0
        for link in links_to_comment:
            if(link!=""):
                driver.get(link)
                #all_reviews_btn=driver.find_element_by_css_selector(".see-all-reviews a")
                #all_reviews_btn.click()
                sleep(10)
                comment_overlay=driver.find_element_by_css_selector(".reviews-overlay")
                #maintenant nous devons connaitre le nombre total de commentaire
                total_comment=driver.find_element_by_css_selector(".reviews-overlay .total-count-number").text

                total_comment=int(total_comment)
                loop_num=total_comment//50
                page_comment=0;
                stop_condition=True
                while stop_condition:
                    all_reviews_card=driver.find_elements_by_css_selector(".brand-reviews-listing .review-card")
                    #Pour chaque carte on extrait le commentaire
                    commentservice=CommentService()
                    for review_card in all_reviews_card:
                        comment=Comment()
                        comment.text=review_card.find_element_by_css_selector("blockquote.description").text
                        comment.website=self.website
                        comment.hotel=nhotel
                        comment_date=review_card.find_element_by_css_selector(".card-header .date").text
                        comment_date=comment_date.replace("Check-in ","")
                        comment_date=dateparser.parse(comment_date)
                        comment.add_date=comment_date
                        comment_add=commentservice.add(comment)
                    #endfor
                    if loop_num==page_comment:
                        stop_condition=False
                    page_comment=page_comment+1
                    #maintenant nous recherchons le boutton suivant
                    try:
                        link_to_next_comment_page=driver.find_element_by_css_selector(".reviews-overlay .pagination-controls a.cta-next")
                        link_to_next_comment_page.click()
                        sleep(5)
                    except:
                        pass

            i=i+1

            
        return driver
    def parse_specific_hotel(self,hotel_name):
        driver=webdriver.Firefox()
        return driver

