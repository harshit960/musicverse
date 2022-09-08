
from django.db import models

 


class history(models.Model):
  hid = models.IntegerField(auto_created=True,primary_key=True)
  title = models.CharField(max_length=255)
  ytlink = models.CharField(max_length=255)
  dtlink = models.TextField()
  tags = models.TextField()
  user = models.IntegerField(null=True)
  def __str__(self):
        return self.title
