from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_data = models.DateField(null=True)
    read_count = models.SmallIntegerField(default=0)
    commentcount = models.SmallIntegerField(default=0)
    is_delete = models.BooleanField(default=False)
class People(models.Model):
    pass
