
from django.db import models

# Create your models here.


class data(models.Model):
    training = models.IntegerField()
    testing = models.IntegerField()
    describe = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    file = models.FileField(blank=True, null=True)

    def __unicode__(self):
        return str(self.id) + " <-> " + self.email
