from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100)
    respiration_rate = models.FloatField()
    body_temperature = models.FloatField()
    blood_oxygen_levels = models.FloatField()
    eye_movement = models.FloatField()
    hours_of_sleep = models.FloatField()
    sleep_rate = models.FloatField()

    def __str__(self):
        return self.name
    
    