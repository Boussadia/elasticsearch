from django.db import models

# Create your models here.

class Author(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)

	def __unicode__(self):
		return '%s %s'%(self.first_name, self.last_name)

class Book(models.Model):
	author = models.ForeignKey(Author)
	title = models.CharField(max_length = 100)

	def __unicode__(self):
		return '%s by %s'%(self.title, self.author)
