# from unicodedata import category
import email
from django.db import models
from pyexpat import model
from re import T
import uuid
from django.db import models
from django.contrib.auth.models import  User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

# Create your models here.

# class CategoryAcc(models.Model):
#     name=models.CharField(max_length=255)
#     def __str__(self):
#          return self.name

#     def get_absolute_url(self):
#     # return reverse('article_detail',args=[str(self.pk)])
#         return reverse('homeview')





class Post(models.Model):
    # title_tag=models.CharField(max_length=255,default="E-Healthcare")
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255,default="E-Healthcare")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    # body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    category= models.CharField(max_length=255,default='Mental Therapy')
    snippet= models.CharField(max_length=255,default='CLick the link above to see the Content..')

    def __str__(self):
        return self.title + ' | '+str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article_detail',args=[str(self.pk)])
        return reverse('homeview')

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)
    def get_absolute_url(self):
        # return reverse('update_view',args=[str(self.pk)])
         return reverse('homeview')
        

class Contact(models.Model):
    name= models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    body=models.TextField()
    
    def get_absolute_url(self):
        
        return reverse('contact')


class Appointment(models.Model):
    
    name= models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    phonenumber=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    doc_name=models.CharField(max_length=255)

    # def __str__(self):
    #     return '%s - %s' % (self.post.title,self.name)
    def get_absolute_url(self):
        # return reverse('update_view',args=[str(self.pk)])
         return reverse('homeview')

class Prescription(models.Model):
    Patient_name= models.CharField(max_length=255)
    patient_age=models.IntegerField()
    medicine= models.CharField(max_length=255)
    date_added=models.DateTimeField(auto_now_add=True)
    doc_name=models.CharField(max_length=255)
    patient_disease= models.CharField(max_length=255)
    advice=models.TextField()
    def get_absolute_url(self):
    # return reverse('update_view',args=[str(self.pk)])
     return reverse('prescription')




   
    
