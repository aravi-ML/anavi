from .models import Expert,models


class ExpertService:

    def __init__(self):
        pass

    def count(self):
        """Return the number of service """
        return Expert.objects.aggregate(nb=models.Count("id"))["nb"]