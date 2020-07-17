from .model.website import WebSite
class WebSiteService:
    def __init__(self):
        pass
    
    def add(self,website):
        response={"state":False,"msg":"Website have already same name","website":None}
        website_exist=WebSite.objects.filter(name__iexact=website.name)
        if(len(website_exist)==0):
            response["state"]=True
            response["msg"]="Website add with success"
            website.save()
            response["website"]=website
        else:
            response["website"]=website_exist[0]
        return response
    
    def count(self):
        """return the number of website crawl by us """
        return len(WebSite.objects.all())