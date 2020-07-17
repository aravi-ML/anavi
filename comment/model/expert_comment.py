from django.db import models
from .comment import *
from anaviexpert.model.expert import Expert

class ExpertComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,null=True)
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE,null=True)
    label = models.CharField(max_length=200)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

admin.site.register(ExpertComment)