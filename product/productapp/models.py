from django.db import models

# Create your models here.
class productmodel(models.Model):
	pname = models.CharField(max_length=20)
	pprice = models.IntegerField()
	pcategory = models.CharField(max_length=20)
	pdescription = models.CharField(max_length=20)

	def __str__(self):
		return self.pname