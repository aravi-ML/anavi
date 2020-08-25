from .models import Searcher,models


class SearcherService:

    def __init__(self):
        pass

    def count(self):
        """return the number of searher of anavi"""
        return Searcher.objects.aggregate(nb=models.Count("id"))["nb"]