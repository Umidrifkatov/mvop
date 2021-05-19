from django.db import models



class patient(models.Model):
    key = models.CharField(null=False, max_length=64)
    age = models.IntegerField(null=True)
    sex = models.BooleanField(default=False, null=True)
    xray = models.IntegerField(null=True)
    c_react = models.BooleanField(default=False, null=True)
    comp = models.IntegerField(null=True)
    compc = models.CharField(null=True, max_length=100)
    bmi = models.BooleanField(default=False, null=True)
    sinovit = models.BooleanField(default=False, null=True)
    echt = models.BooleanField(default=False, null=True)



