from django.db import models
from django.contrib.auth.hashers import make_password

class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='treatments',null=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128, null=True)  # Store hashed passwords
    email = models.EmailField(max_length=100, unique=True, null=True)  # Use EmailField for emails
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, related_name='users',null=True)  # ForeignKey to Disease
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name='users',null=True)  # ForeignKey to Treatment

    def save(self, *args, **kwargs):
        # Hash the password before saving
        if self.password and not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
