from .models import Employee

def getEmployee(username,password):
    obj=Employee.objects.filter(username=username,password=password)
    return obj
