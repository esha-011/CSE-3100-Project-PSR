from importlib.resources import contents
from tkinter import Image
from turtle import title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField( default='Any', upload_to = 'myphoto')

    def __str__(self):
         return self.title
          
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


    def save(self):
        super().save()

        img1 = Image.open(self.photo.path)
        if img1.height > 500 or img1.width >900:
            output_size = (500, 900)
            img1.thumbnail(output_size)
            img1.save(self.photo.path)




    


