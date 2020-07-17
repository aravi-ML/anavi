from .model.expert import Expert


class ExpertService:

    def __init__(self):
        pass

    def count(self):
        """Return the number of service """
        return len(Expert.objects.all())