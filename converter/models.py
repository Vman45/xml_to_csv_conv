from django.db import models

class Request(models.Model):
	series = models.CharField(max_length=100)
	studio = models.CharField(max_length=100)
	directory = models.CharField(max_length=150)
	date_requested = models.DateField(auto_now_add=True)
	export_csv = models.BooleanField(default=False)
	save_csv = models.BooleanField(default=False)
	filename = models.CharField(max_length=50, default='compiled_xmls')

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

