from django.db import models

class Doctor(models.Model):
    doctor_name=models.CharField(max_length=150)
    mobile_no=models.IntegerField()
    specialization=models.CharField(max_length=100)
    experience=models.CharField(max_length=50)

    shift_choices=(
    ('day shift','Day Shift'),
    ('night shift','Night Shift')
    )
    shift=models.CharField(max_length=30,choices=shift_choices)
