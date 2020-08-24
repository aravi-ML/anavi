from .model.manager import Manager
from anaviuser.model.user import User
from hotel.model.hotel import Hotel


class ManagerService:
    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    def get_managed_hotel(cls,user):
        managers_list=Manager.objects.filter(user=user,state=True)
        return managers_list
    
    @classmethod
    def get_ask_demand(cls,manager,state=False):
        ask_demand=manage.ask_manage_set.all()
        ask_demand=ask_demand.filter(state=state)
        return ask_demand

    