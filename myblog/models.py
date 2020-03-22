from django.db import models
from django.utils.text import slugify
from time import time

def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug+'-'+str(int(time()))

class Post(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, blank=True, unique=True)
	body = models.TextField(blank=True, db_index=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(upload_to='images/', blank=True)

	def __str__(self):
		return '{}'.format(self.title)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)


	class Meta:
		ordering = ['-date_pub']


class Feedback(models.Model):
	title = models.CharField(max_length=150, db_index=True, default="tmp")
	slug = models.SlugField(max_length=150, blank=False)
	body = models.TextField(blank=False, db_index=True)

	def save(self, *args, **kwargs):
		self.slug = gen_slug((self.body).split(" ")[0])
		self.title = self.slug
		super().save(*args, **kwargs)

	def __str__(self):
		return '{}'.format(self.title)


class Project(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, blank=True)
	body = models.TextField(blank=True, db_index=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	image1 = models.ImageField(upload_to='images/', blank=True)
	image2 = models.ImageField(upload_to='images/', blank=True)	
	image3 = models.ImageField(upload_to='images/', blank=True)		
	 	 
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*args, **kwargs)


	def __str__(self):
		return '{}'.format(self.title)


	class Meta:
		ordering = ['-date_pub']
		

class Article(object):
 	pass

