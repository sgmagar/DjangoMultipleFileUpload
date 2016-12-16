from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField('Full Name of Person',max_length=100)
	Age = models.PositiveIntegerField()

	def __unicode__(self):
		return self.name

class PersonPhoto(models.Model):
	photo = models.FileField('Photos of Person',upload_to='image')

	def __unicode__(self):
		return self.photo
