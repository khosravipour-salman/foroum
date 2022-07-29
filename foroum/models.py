from django.db import models
from django.template.defaultfilters import slugify
from accounting.models import CustomUser


class Room(models.Model):
	title = models.CharField(max_length=32)
	profile_image = models.ImageField(null=True, blank=True)
	owner = models.ManyToManyField(CustomUser, related_name='owner_rooms')
	bio = models.TextField(null=True, blank=True)
	
	slug = models.SlugField()

	create = models.DateTimeField(auto_now_add=True)
	modify = models.DateTimeField(auto_now=True)
	
	members = models.ManyToManyField(
		CustomUser, related_name='member_rooms', blank=True
	)
	
	def save(self, *args, **kwargs):
	    self.slug = slugify(self.title)
	    return super(Room, self).save(*args, **kwargs)

	def __str__(self):
		return self.title


class Post(models.Model):
	title = models.CharField(max_length=32)
	content = models.TextField()
	post_image = models.ImageField()
	room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='posts')

	create = models.DateTimeField(auto_now_add=True)
	modify = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_comments')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
	text = models.TextField()

	def __str__(self):
		return self.text + ' from ' + self.user.email


class Like(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_likes')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes') 
	vote = models.BooleanField()

	def __str__(self):
		return self.vote + ' from ' + self.user.email
