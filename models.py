from django.db import models

# Create your models here.
class stol(models.Model):
    jednostki = models.CharField(max_length=1)
    dziesiatki = models.CharField(max_length=1)
    linia = models.CharField(max_length=1)
    zmiana = models.BooleanField(default=False)
    czas_start=models.TimeField(null=True,blank=True)
    dataczas_start=models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return str(' / ').join((self.dziesiatki, self.jednostki, self.linia))

class stol_pr(models.Model):
    jednostki = models.CharField(max_length=1)
    dziesiatki = models.CharField(max_length=1)
    linia = models.CharField(max_length=1)
    def __str__(self):
        return str(' / ').join((self.dziesiatki, self.jednostki, self.linia))
