from django.db import models
import datetime as dt 
from users.models import Profile
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
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
    
    def update_project(self, **kwargs):
        self.objects.filter(project_description).update(**kwargs)

    class Meta:
        ordering = ['-pub_date']    

    @classmethod
    def search_profile(cls,search_term):
        profiles = cls.objects.filter(Q(username__username=search_term))
        return profiles
    @classmethod
    def todays_projects(cls,date):
       projects = cls.objects.filter(pub_date__date = date)
       return projects
