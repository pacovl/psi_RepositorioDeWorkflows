from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
import datetime

class Category(models.Model):
    """ This class defines the structure of a Category object in the database.
    """
    name = models.CharField(max_length=128, unique=True, null=False)
    slug = models.SlugField(unique=True)
    created = models.DateField()
    tooltip = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.created = datetime.datetime.now()
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
    def __unicode__(self): # For Python 2, use __unicode__ too
        return self.name

class Workflow(models.Model):
    """ This class defines the structure of a Category object in the database.
    """
    name = models.CharField(max_length=128, unique=True, null=False)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=512, default="")
    views = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)
    versionInit = models.CharField(max_length=128, default="")
    category = models.ManyToManyField(Category, blank= False)
    client_ip = models.GenericIPAddressField(default="0.0.0.0")
    keywords = models.CharField(max_length=256, default="")
    json = models.CharField(max_length=8192)
    created = models.DateField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.created = datetime.datetime.now()
        super(Workflow, self).save(*args, **kwargs)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.name
    def __unicode__(self): # For Python 2, use __unicode__ too
        return self.name