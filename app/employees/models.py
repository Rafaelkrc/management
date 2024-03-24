from django.db import models


class Countries(models.Model):
    country = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)
    continent = models.CharField(max_length=50)


class State(models.Model):
    state = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)
    country = models.ForeignKey(Countries, on_delete=models.PROTECT, related_name='state_country')
    region = models.CharField(max_length=20)


class Cities(models.Model):
    city = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='city_state')


class Job(models.Model):
    job = models.CharField(max_length=30)
    description_job = models.TextField()


class Employees(models.Model):
    identifier = models.CharField(max_length=14)
    full_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=10, blank=True, null=True)
    address_street = models.CharField(max_length=50)
    address_number = models.CharField(max_length=7)
    postal_code = models.CharField(max_length=10)
    city = models.ForeignKey(Cities, on_delete=models.PROTECT, related_name='employees_city')
    telephone_number = models.CharField(max_length=15, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    position_job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name='employees_job', blank=True, null=True)
    date_of_registration = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='employees/', blank=True, null=True)
