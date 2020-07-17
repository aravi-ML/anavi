from anaviuser.model.user import User
class UserService:
    def __init__(self):
        pass

    def count(self):
        """Return the total number of user in our system """
        return len(User.objects.all())