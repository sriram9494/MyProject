from django.contrib import admin
from .models import Employee, Student, Customer, Account, Course, StudentDetails
from .models import Addr
from .models import Emp
from django.contrib import admin
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','firstName', 'lastName', 'age', 'username', 'password','created_date')

admin.site.register(Employee, EmployeeAdmin)

###################################
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','firstName', 'lastName', 'rollNo', 'branch', 'age','dob','created_date')

admin.site.register(Student,StudentAdmin)

#######################################################################################


class MyAddradmin(admin.ModelAdmin):
   		list_display = ('id','street','city','country','zip')

class MyEmpadmin(admin.ModelAdmin):
   		list_display = ('id','firstName', 'lastName','currAddr')


admin.site.register(Addr, MyAddradmin)
admin.site.register(Emp, MyEmpadmin)

#########################
class MyCustomeradmin(admin.ModelAdmin):
   		list_display = ('id','name','age')
class MyAccountadmin(admin.ModelAdmin):
   		list_display = ('id','name','custId','created_date')


admin.site.register(Customer, MyCustomeradmin)
admin.site.register(Account, MyAccountadmin)

#######################
class MyStudentadmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'mobileNo')


class MyCourseadmin(admin.ModelAdmin):
	list_display = ('id', 'courseName')

admin.site.register(StudentDetails, MyStudentadmin)
admin.site.register(Course, MyCourseadmin)



