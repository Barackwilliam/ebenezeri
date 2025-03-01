from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

class TeamMember(models.Model):
    full_name = models.CharField(max_length=255)
    image = CloudinaryField('image', blank=True, null=True) 
    designation = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    

class New_Update(models.Model):
    DESIGNATION_CHOICE = [
        ('Mwenyekiti','Mwenyekiti'),
        ('Katibu','Katibu'),
        ('Mhasibu','Mhasibu'),
    ]
    date = models.DateField()
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICE)
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True) 
   
    def __str__(self):
        return self.full_name
    



class Course_Category(models.Model):
    Course_type = models.CharField(max_length=500)
    Total_courses = models.IntegerField()
    image = CloudinaryField('image', blank=True, null=True) 

    def __str__(self):
        return self.Course_type
    

class Popular_Course(models.Model):
    Course_name = models.CharField(max_length=500)
    Student_enroll = models.IntegerField()
    Price = models.IntegerField()
    image = CloudinaryField('image', blank=True, null=True) 
    def __str__(self):
        return self.Course_name
    

class Student_testimonial(models.Model):
    Student_name = models.CharField(max_length=255)
    Profession = models.CharField(max_length=255)
    content = models.TextField()
    profile = CloudinaryField('image', blank=True, null=True) 
    def __str__(self):
        return self.Student_name
    

class Course_gallery(models.Model):
    image_name = models.CharField(max_length=255)
    Course_image = CloudinaryField('image', blank=True, null=True) 
    def __str__(self):
        return self.image_name
    

class Service(models.Model):
    Title = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.Title


class Message(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.full_name

    
class User_Testimonial(models.Model):
    full_name = models.CharField(max_length=255)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True) 
    def __str__(self):
        return self.full_name


class Direct_Service(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    service_type = models.CharField(max_length=255)
    phone_number = models.IntegerField(max_length=12)

    def __str__(self):
        return self.full_name
    