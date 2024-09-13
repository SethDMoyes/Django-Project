#from django.db import models

# Create your models here.


#class Post(models.Model):
 #   title = models.CharField(max_length=50)
 #   description = models.TextField()
  #  deadline = models.DateField()

  #  def __str__(self):
  #      return self.title

from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class ToDo(models.Model):
    title=models.CharField(max_length=200,validators=[MinLengthValidator(3,"Todo name must contain at least 3 characters")])
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title
