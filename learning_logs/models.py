from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
	"""A topic the user is learning about"""
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text


class Entry(models.Model):
	"""Something specific learned about a topic"""
	topic = models.ForeignKey(Topic)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		text_to_show = self.text
		if len(text_to_show) > 50:
			text_to_show = self.text[:50] + "..."
		return text_to_show
