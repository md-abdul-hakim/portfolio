from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile', blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    facebook = models.URLField(max_length=1000)
    twitter = models.URLField(max_length=1000)
    github = models.URLField(max_length=1000)
    linkedin = models.URLField(max_length=1000)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class About(models.Model):
    image = models.ImageField(upload_to='about', blank=True)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description[:55]
    
class Service(models.Model):
    logo = models.CharField(max_length=255)
    tittle = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.tittle
    
SKILL_CATEGORY = (
    ('technical', 'Technical'),
    ('professional', 'Professional')
)

class Skill(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=SKILL_CATEGORY, default='technical')
    proficiency = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class Education(models.Model):
    institute = models.CharField(max_length=255, blank=True)
    degree = models.CharField(max_length=255, blank=True)
    started_at = models.IntegerField()
    end_at = models.IntegerField()
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.degree

class Experience(models.Model):
    institute = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=1000)
    started_at = models.DateTimeField()
    end_at = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.institute    
    
class Message(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Location(models.Model):
    address = models.CharField(max_length=255)
    date = models.DateField(blank=True)
    
    def __str__(self):
        return self.address
    
class Category(models.Model):
    name = models.CharField(max_length=55)
    
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog')
    tittle = models.CharField(max_length=255, blank=True)
    sub_tittle = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.tittle