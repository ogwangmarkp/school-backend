from django.db import models
from django.utils import timezone
from school.models import School
# Create your models here.
class Student(models.Model):
    GENDER = (('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        )
    date_added = models.DateTimeField(default = timezone.now)
    name = models.CharField(max_length = 255, null=False, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    other_phone  = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length = 50, null=True, blank=True)
    profile_url = models.TextField(blank=True, null=True)
    dob =  models.DateField( null=True, blank=True)
    nin = models.CharField(max_length = 20, null=True, blank=True)
    nationality = models.CharField(max_length = 255, default="Ugandan")
    gender = models.CharField(max_length = 25, choices=GENDER,default="O")
    marital_status = models.CharField(max_length = 255, null=True, blank=True)
    student_number = models.CharField(max_length = 50, null=True, blank=True)
    added_by = models.BigIntegerField(null=True, blank=True)
    status     =  models.CharField(max_length=25, null=True, blank=True)
    is_active  = models.BooleanField(default=True)
    student_school =  models.ForeignKey(School, on_delete=models.CASCADE, related_name='student_school')
    
    def __str__(self):
        return self.name