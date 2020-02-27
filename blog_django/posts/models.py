from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=2000)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

#Python2
    # def __unicode__(self):
    #     return self.title

#Python3
    def __str__(self):
        return self.title
