from django.core.paginator import Paginator
from .model.comment import *

class CommentService:
    
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


    