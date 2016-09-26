from django.db import models
from django.utils.encoding import smart_text



class SqrtNumber(models.Model):
    number = models.IntegerField(max_length=255)
    sqrt = models.IntegerField(max_length=255, blank=True, null=True)

    def __str__(self):
        return smart_text(self.number)