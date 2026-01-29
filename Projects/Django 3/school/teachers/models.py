from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.email} - {self.subject} {self.phone}"