from django.db import models

class Request(models.Model):
	studio = models.CharField(max_length=100)
	directory = models.CharField(max_length=150)
	date_requested = models.DateField(auto_now_add=True)

	#file
	#user

	def __str__(self):
		return self.directory

# String series name
# Int season number
# Int episode count
# Date monthly order table / schedule month
# Bool complete
# All Metadata Fields?

