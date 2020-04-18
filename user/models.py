from PIL import Image
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    # Profile has one to one relationship with User
    # One User has one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=10, default='Not Available')
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        # Show in this format in DB like admin's profile
        return f"{self.user.username}'s profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)
