from django.core.paginator import Paginator
from django.db.models import Q,F
from .models import *
from googletrans import Translator
import langdetect
import requests
import json
try:
    import translators as ts
except:
    pass
import random
import datetime
from django.utils import timezone
class CommentService:
    def translate(self,text,to_lang="en"):
        translation=""
        try:
            translation=ts.google(text,to_language=to_lang)
        except:
            try:
                translation=ts.deepl(text,to_language=to_lang)
            except:
                try:
                    translation=ts.bing(text,to_language=to_lang)
                except:
                    try:
                        translation=ts.baidu(text,to_language=to_lang)
                    except:
                        try:
                            translation=ts.alibaba(text,to_language=to_lang)
                        except:
                            try:
                                translation=ts.sogou(text,to_language=to_lang)
                            except:
                                try:
                                    translation=ts.tencent(text,to_language=to_lang)
                                except:
                                    pass
        return translation
                    

    def if_exist(self,comment):
        comment_list=Comment.objects.filter(text__iexact=comment.text,hotel=comment.hotel,website=comment.website,add_date=comment.add_date)
        lenght=len(comment_list)
        if(lenght>0):
            return True
        else:
            return False
    def add(self,comment):
        response={"status":False,"msg":"Comment add with success"}
        if(self.if_exist(comment)==False):
            response['status']=True
            comment.save()
            response["comment"]=comment
        else:
            response["msg"]="Comment already exist"
        return response
    
    def get_unique_comment(self):
        comments=Comment.objects.all()
    

    def count(self):
        """Function who return all the number of comment"""
        comments=Comment.objects.all()
        nb_comment=len(comments)
        return nb_comment
    
    def get_comment_page_list(self,num_page=1,number_per_page=10):
        """By default we are on page 1 and we take 50 comments per 
        page"""
        comments=Comment.objects.filter(~Q(text__iexact=""))
        comments=list(comments)
        comments_pages=Paginator(comments,number_per_page)
        #comments_pages=list(comments_pages)
        comment_page=comments_pages.page(num_page).object_list
        return comment_page
    
    def pretaired_google(self):
        all_comment=Comment.objects.filter(Q(text__icontains='(translated by google)') | Q(text__icontains='(original)'))
        for comment in all_comment:
            ##commentcons par supprimez le translate by google
            com_t=comment
            com_t.text=comment.text.replace("(Translated by Google)","")
            com_t.text=com_t.text.replace("\n","")
            #maintenant on va faire un split en fonction de (original)
            diffrent_text=com_t.text.split("(Original)")
            #print(diffrent_text)
            #Si la taille veau 2 allors le texte origanl est en 1 et le traduit en 0
            lang0=langdetect.detect(diffrent_text[0])
            if(len(diffrent_text)==2):
                com_t.text=diffrent_text[1]
                try:
                    com_t.text_lang=langdetect.detect(com_t.text)
                    if(com_t.text_lang=="en"):
                        com_t.text_en=com_t.text
                    #on fait une traduction en francais maintenant avec google transalte
                    elif(com_t.text_lang=="fr"):
                        com_t.text_fr=com_t.text
                except:
                    com_t.text=diffrent_text[0]
            
                if(lang0=="fr"):
                    com_t.text_fr=diffrent_text[0]
                elif(lang0=="en"):
                    com_t.text_en=diffrent_text[0]
            #maintenant si le split n'existe pas
            else:
                com_t.text=diffrent_text[0]
                if(lang0=="fr"):
                    com_t.text_fr=diffrent_text[0]
                elif(lang0=="en"):
                    com_t.text_en=diffrent_text[0]
            ##maintenant nous devons faire une traduction des texte
            if(com_t.text_fr==""):
                com_t.text_fr=self.translate(com_t.text,to_lang="fr")
            if(com_t.text_en==""):
                com_t.text_en=self.translate(com_t.text,to_lang="en")

            com_t.save()      


    def setlanguage_to_all_comment(self):
        #recuperation des commentaires qui n'ont pas de langue
        all_not_tag_comment=Comment.objects.exclude(Q(text=None)|Q(text=""))
        all_not_tag_comment=all_not_tag_comment.filter(text_lang=None)
        not_tr=[]
        for comment in all_not_tag_comment:
            try:
                lang=langdetect.detect(comment.text)
                comment.text_lang=lang
                if(lang=="fr"):
                    comment.text_fr=comment.text
                if(lang=="en"):
                    comment.text_en=comment.text
            
                comment.save()
            except:
                not_tr.append(comment.id)
        return not_tr

    def traid_other(self,):
        all_not_tag_comment=Comment.objects.exclude(Q(text=None)|Q(text=""))
        all_not_tag_comment=all_not_tag_comment.exclude(Q(text_lang="fr") | Q(text_lang="en"))
        
        gtrans=Translator()
        for comment in all_not_tag_comment:
            try:
                lang=gtrans.detect(comment.text)
                langue=lang.lang
                if(langue=="fr" or langue=="en"):
                    comment.text_lang=langue
                    if(langue=="fr"):
                        comment.text_fr=comment.text
                    else:
                        comment.text_en=comment.text
                comment.save()
            except:
                pass
    
    #maintenant nous devons faire les traductions des commentaires en francais et en anglais
    def translate_all_comment(self):
        #selctionnons d'abord les commentaires qui n'ont pas leur version francaise
        all_not_tag_comment=Comment.objects.exclude(Q(text=None)|Q(text=""))
        all_not_fr=all_not_tag_comment.filter(text_fr=None)
        gtrans=Translator()
        for comment in all_not_fr:
            try:
                text_fr=gtrans.translate(comment.text,dest="fr").text
                comment.text_fr=text_fr
                comment.save()
            except:
                pass
        #on va selctionner tous les commentaires qui n'ont pas la langue anglaise
        all_not_en=all_not_tag_comment.filter(text_en=None)
        for comment in all_not_en:
            try:
                text_en=gtrans.translate(comment.text,dest="en").text
                comment.text_en=text_en
                comment.save()
            except:
                pass

    
    def set_random_date(self):
        comments=Comment.objects.filter(add_date__year=2020,add_date__month=6, add_date__day__gte=17)
        for comment in comments:
            day=random.randint(1,28)
            month=random.randint(1,12)
            year=random.randint(2010,2020)
            date_comment=timezone.datetime(year,month,day,0,0,0)
            comment.add_date=date_comment
            comment.save()


    ##defintion des fonctions de postagging
    def post_tag_tofrench_all(self):
        comment_list=[]
        comments=Comment.objects.exclude(Q(text=None)|Q(text="")|Q(text_lang=None)).filter(id__gt=14294)
        for comment in comments:
            all_tag=requests.post('http://[::]:9000/?properties={"annotators":"tokenize,ssplit,pos", "tokenize.language":"fr","outputFormat":"json"}', data ={'data':comment.text_fr}).text
            all_tag_json=json.loads(all_tag)
            try:
                if(all_tag_json["sentences"][0]["tokens"][0]["word"]=="data"):
                    all_tag_json["sentences"][0]["tokens"].pop(0)
                if(all_tag_json["sentences"][0]["tokens"][0]["word"]=="="):
                    all_tag_json["sentences"][0]["tokens"].pop(0)
            except:
                comment_list.append(comment.id)
            i=0
            for sentence in all_tag_json["sentences"]:
                #on parcours les differens tokens et on recupere les 
                #differents pos==NN ou pos==NNS
                an_aspect=False
                for tags in sentence["tokens"]:
                    if(tags["pos"]=="NOUN"):
                        an_aspect=True
                        aspect=Aspect(name_fr=tags["word"],start_to=tags["characterOffsetBegin"]-5,end_to=tags["characterOffsetEnd"]-5,comment=comment,sentence_index=i)
                        try:
                            aspect.save()
                        except:
                            comment_list.append({"text":tags["word"],"id":comment.id})
                            return comment_list

                i=i+1
        return comment_list
    
    def posttag_english(self):
        comments=Comment.objects.exclude(Q(text=None)|Q(text="")|Q(text_lang=None)).filter(id__gte=16606)
        comment_list=[]
        for comment in comments:
            all_tag=requests.post('http://[::]:9000/?properties={"annotators":"tokenize,ssplit,pos", "tokenize.language":"fr","outputFormat":"json"}', data ={'data':comment.text_en}).text
            all_tag_json=json.loads(all_tag)
            try:
                if(all_tag_json["sentences"][0]["tokens"][0]["word"]=="data"):
                    all_tag_json["sentences"][0]["tokens"].pop(0)
                if(all_tag_json["sentences"][0]["tokens"][0]["word"]=="="):
                    all_tag_json["sentences"][0]["tokens"].pop(0)
            except:
                comment_list.append(comment.id)
            i=0
            for sentence in all_tag_json["sentences"]:
                #on parcours les differens tokens et on recupere les 
                #differents pos==NN ou pos==NNS
                an_aspect=False
                for tags in sentence["tokens"]:
                    if(tags["pos"]=="NN"):
                        an_aspect=True
                        aspect=AspectEn(name_en=tags["word"],start_to=tags["characterOffsetBegin"]-5,end_to=tags["characterOffsetEnd"]-5,comment=comment,sentence_index=i)
                        try:
                            aspect.save()
                        except Exception as e:
                            comment_list.append({"text":tags["word"],"id":comment.id,"msg":str(e)})
                            return comment_list

                i=i+1
        return comment_list
