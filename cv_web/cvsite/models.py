from django.db import models
import datetime


class cvelement(models.Model):
    nome = models.CharField(max_length=100, default=None)
    descrizione = models.CharField(max_length=60, default=None)
    riassunto = models.CharField(max_length=500, default=None)
    start = models.DateField(("Date"), default=datetime.date.today)
    end = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.nome