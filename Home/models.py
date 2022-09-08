
from django.db import models


class reg_user(models.Model):
  id = models.IntegerField(auto_created=True,primary_key=True)
  email = models.CharField(max_length=255,blank=True)
  Name = models.CharField(max_length=255,blank=True)
  Password = models.CharField(max_length=50,blank=True)
  tags = models.TextField()
  


class history(models.Model):
  hid = models.IntegerField(auto_created=True,primary_key=True)
  title = models.CharField(max_length=255)
  ytlink = models.CharField(max_length=255)
  dtlink = models.TextField()
  tags = models.TextField()
  user = models.IntegerField(null=True)
  def __str__(self):
        return self.title
