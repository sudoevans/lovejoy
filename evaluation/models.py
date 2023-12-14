# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User
#import abstractuser

# Dro[ down menu for contact method]
CONTACT_METHOD = (
    ('email', 'Email'),
    ('phone', 'Phone'),
)


class EvaluationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHOD)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

