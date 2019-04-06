# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#patient(id , nameP)
#doctor(id,nameD)
#prescription(id,doctor(id)⇑,patient(id)⇑,)

class Patient(models.Model):
    """ This class defines the structure of a <> object in the database.
    """
    nameP = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        super(Patient, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Patients'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.nameP
    def __unicode__(self): # For Python 2, use __unicode__ too
        return self.nameP

class Doctor(models.Model):
    """ This class defines the structure of a <> object in the database.
    """
    nameD = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        super(Doctpr, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Doctors'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.nameD
    def __unicode__(self): # For Python 2, use __unicode__ too
        return self.nameD

class Presciption(models.Model):
    """ This class defines the structure of a <> object in the database.
    """
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)

    def save(self, *args, **kwargs):
        super(Presciption, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Presciptions'

    def __str__(self): # For Python 2, use __unicode__ too
        return str(self.id)
    def __unicode__(self): # For Python 2, use __unicode__ too
        return str(self.id)
