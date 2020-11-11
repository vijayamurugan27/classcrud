from django.db import models

from django.urls import reverse

class Shop(models.Model):
	title = models.CharField(max_length = 250)
	description = models.CharField(max_length = 250, blank = True, null = True)
	Owner = models.CharField(max_length = 250, blank = True, null = True)
	
	def __str__(self):
		return self.title

#	def get_absolute_url(self):
#		return reverse('shop-title', kwargs = {'pk': self.pk})