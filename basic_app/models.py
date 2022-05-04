from django.db import models


# Create your models here.


class Procids(models.Model):
    name = models.CharField(max_length=300)
    phone = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return f"name: {self.name}\nphone: {self.phone}\nmessage: {self.message}"
