from django.db import models

class appt(models.Model):
    date=models.CharField(max_length=10)
    time=models.TimeField()

    def __str__(self):
        return self.date
