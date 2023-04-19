from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
import datetime
# Create your models here.


class Task(models.Model):
  categories = [
    ("Urgent and important", "Urgent and important"),
    ("Not urgent but important", "Not urgent but important"),
    ("Urgent but not important", "Urgent but not important"),
    ("Not urgent and not important", "Not urgent and not important"),
  ]
  
  title = models.CharField(max_length=100, null=False, blank=False)
  description = models.TextField()
  image = models.ImageField(upload_to='tasks_images', null=True, blank=True)
  complete = models.BooleanField(default=False)
  category = models.CharField(max_length=50, verbose_name='task category',
    default='Urgent and important', null=False, blank=False, choices=categories)
  author = models.ForeignKey(
      User, on_delete=models.CASCADE, null=False, blank=False)
  created_date = models.DateTimeField(auto_now_add=True)
  deadline = models.DateTimeField(null=False, blank=False)
  
  def __str__(self):
    return self.title
  
  @property
  def task_image(self):
    try:
      url = self.image.url
    except:
      url=''
    return url
  
  # Check if the deadline is about to end or has already ended.
  @property
  def check_deadline(self):
    task_status = self.complete
    now = timezone.now()
    time_diff = self.deadline - now
    if task_status != True and (time_diff > datetime.timedelta(hours=0) and time_diff < datetime.timedelta(hours=24) and now < self.deadline):
      return 'about' # This means that the deadline doesn't pass yet.
    elif task_status != True and now > self.deadline:
      return 'ended' # This means that the deadline has been passed.
    elif task_status != True and (time_diff > datetime.timedelta(hours=0) and time_diff > datetime.timedelta(hours=24) and now < self.deadline):
      return 'more'  # This means that the deadline has more than 24 hours to end.
  
  def get_absolute_url(self):
    return reverse("task_detail", kwargs={"pk": self.pk})