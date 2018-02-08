from django.db import models
from django.utils.text import slugify
from django.contrib.postgres.fields import JSONField


class Snippet(models.Model):
	"""
	TODO: Convert result to JSONField
	"""
	date = models.DateTimeField()
	share_code = models.CharField(max_length=100)
	slug = models.SlugField(unique=True)
	result = JSONField()
	code = models.TextField()

	def __str__(self):
		return self.share_code

	def save(self, *args, **kwargs):
		self.slug = slugify(self.share_code)
		return super(Snippet, self).save(*args, **kwargs)
