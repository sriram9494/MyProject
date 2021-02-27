from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.IntegerField(default=-1)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    count = models.IntegerField(default=0)
####################################################################
#Student Class for student table
class Student(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    rollNo = models.CharField(max_length=20)
    branch=models.CharField(max_length=30)
    age = models.IntegerField(default=-1)
    dob = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
###############################################################################

#################Address Table###############################
class Addr(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

#Employee Table
class Emp(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    currAddr = models.OneToOneField(Addr, on_delete=models.CASCADE)
################Ont to Many#########################
class Customer(models.Model):
   id = models.AutoField(auto_created=True, primary_key=True)
   name = models.CharField(max_length=50)
   age = models.IntegerField()

   def __str__(self):
       return str(self.id)


class Account(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50)
    custId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

###############################Many to Many##################
class StudentDetails(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30)
    mobileNo = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    courseName = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.courseName

"""class CustomerService(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=8,default="")
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=20,unique=True,default="")
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    dept = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(blank=True,null=True,default='')
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.username"""

