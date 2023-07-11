from distutils.command.upload import upload
from tabnanny import verbose
from turtle import title
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Post Title')
    category = models.CharField(max_length=50, choices=[('0','HTML'), ('1','Javascript'),('2','Python'), ('3','Flutter'),('4','Java'), ('5','Ruby')])
    thumbnail = models.ImageField(upload_to='')
    body = RichTextUploadingField(verbose_name='Compose Content')
    summary = models.TextField(verbose_name='Post Summary')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
