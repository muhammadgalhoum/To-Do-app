from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
  gender_types = [
    ('Male', 'Male'),
    ('Female', 'Female')
  ]
  
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
  name = models.CharField(max_length=100, null=False, blank=False)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True, blank=True)
  gender = models.CharField(default='Male', max_length=6, null=False, blank=False, choices=gender_types)
  
  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url='/static/default.jpg'
    return url
  
  def __str__(self):
    return f"{self.user.username} Profile"