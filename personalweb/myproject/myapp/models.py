from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()  # Field for storing age as an integer
    date = models.DateField()    # Field for storing date

    def __str__(self):
        return self.name
