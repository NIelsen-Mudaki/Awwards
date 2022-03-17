from django.db import models
import datetime as dt 
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image=models.ImageField(default="profile_pics/default.jpeg", upload_to='profile_pics')
    bio=models.CharField(max_length=200, blank=False)
    # projects_posted=models.ForeignKey(Image, on_delete=models.CASCADE)
    contact_information = models.TextField()
    

    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_profile(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

class Image(models.Model):    
    project_title=models.CharField(max_length=60)
    project_description = models.TextField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(default="default.jpeg", upload_to = 'images/')
    project_link=models.CharField(max_length=60, null=False)

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(project_title__icontains=search_term)
        return projects

    def __str__(self):
        return self.project_title

    def save_project(self):
        self.save()
    
    def delete_project(self):
        Image.objects.filter(id = self.pk).delete() 
    
    def update_project(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)
    

    class Meta:
        ordering = ['-pub_date']    

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(username__icontains=search_term)
        return profiles
    @classmethod
    def todays_projects(cls,date):
        projects = cls.objects.filter(pub_date__date = date)
        return projects

class Ratings(models.Model):

    TEN_REVIEWS= (
        ('10', '10'),
        ('9', '9'),
        ('8', '8'),
        ('7', '7'),
        ('6', '6'),
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    project = models.ForeignKey(Image, on_delete=models.CASCADE)
    design = models.PositiveIntegerField(max_length=2, choices=TEN_REVIEWS, default="0")
    usability= models.PositiveIntegerField(max_length=2, choices=TEN_REVIEWS, default="0")
    content = models.PositiveIntegerField(max_length=2, choices= TEN_REVIEWS, default= "0")

