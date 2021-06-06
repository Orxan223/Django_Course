from django.db.models.deletion import CASCADE
from django.db import models
from teachers.models import Teacher

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    slug = models.SlugField(max_length=50,unique=True,null=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    teacher = models.ForeignKey(Teacher,null=True,on_delete=CASCADE)
    category= models.ForeignKey(Category,null=True,on_delete=models.DO_NOTHING)
    name = models.CharField (max_length=200, unique=True)
    tags = models.ManyToManyField(Tag, blank=True,null=True)
    description =models.TextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    date= models.DateTimeField(auto_now=True)
    avaible =models.BooleanField(default=True)


    def __str__(self):
        return self.name