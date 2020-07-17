from .model.searcher import Searcher


class SearcherService:

    def __init__(self):
        pass

    def count(self):
        """return the number of searher of anavi"""
        return len(Searcher.objects.all())