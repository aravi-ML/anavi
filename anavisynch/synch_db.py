from anaviadmin.models import *
from anavibase.models import *
from anaviexpert.models import *
from anaviuser.models import *
from anavisearcher.models import *
from anavimanager.models import *
from comment.models import *
from hotel.models import *
from website.models import *

import demoji
import translators as ts

class SynchroniseDB:

    def make_synch(self,list_db_con,main_db_name='default'):
        """That function take main database and list_db_con['name_1',...,'name_n']
        and synhcronise all data"""
        #On commence d'abord par synchroniser les utilisateurs
        all_user=User.objects.using(main_db_name).all()
        #maintnant on va scynchoniser avec les db en parametre
        for dbname in list_db_con:
            for user in all_user:
                try:
                    user.save(using=dbname)
                except:
                    pass
            #Sycnhronisation des experts
            all_expert=Expert.objects.using(main_db_name).all()
            for expert in all_expert:
                try:
                    expert.save(using=dbname)
                except:
                    pass
            #scynchronisation des managers
            all_manager=Manager.objects.using(main_db_name).all()
            for manager in all_manager:
                try:
                    manager.save(using=dbname)
                except:
                    pass
            #scynchronisation of searcher
            all_searcher=Searcher.objects.using(main_db_name).all()
            for searcher in all_searcher:
                try:
                    searcher.save(using=dbname)
                except:
                    pass
            
            #synchronisation des site webs
            all_website=WebSite.objects.using(main_db_name).all()
            for website in all_website:
                website.save(using=dbname)
            
            #synchronisation des hotels
            all_hotel=Hotel.objects.using(main_db_name)
            for hotel in all_hotel:
                hotel.save(using=dbname)
            
            #synchronistion des hotels_website
            all_wh=HotelWebSite.objects.using(main_db_name).all()
            for wh in all_wh:
                wh.save(using=dbname)
            
            #Synchronisation des commentaires
            all_comment=Comment.objects.using(main_db_name).all()
            comments=[]
            for comment in all_comment:
                try:
                    new_text=comment.text.replace("\\","")
                    if(new_text!=comment.text):
                        comment.text=new_text
                        comment.save()
                    comment.text=demoji.replace(comment.text)
                    comment.save(using=dbname)
                except:
                    new_comment=ts.google(comment.text)
                    comment.text=new_comment
                    comment.save()
                    comments.append(comment.id)
            print(comments)
            #synchronisation des exeperts comments
            all_ec=ExpertComment.objects.using(main_db_name).all()
            for ec in all_ec:
                ec.save()

        

                
