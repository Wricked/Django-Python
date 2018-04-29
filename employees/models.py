from django.db import models

# Create your models here.
# Database of X-factor

#Department database
class Department(models.Model):

    name = models.CharField(max_length=255)

    def __unicode__ (self):
        return self.name

#Employee database
class Employees(models.Model):

    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=75, null=False, unique=True)
    department = models.ForeignKey(Department)

    def __str__ (self):
        return self.name

