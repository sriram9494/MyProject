from django.http import HttpResponse
from django.shortcuts import render
from django.db.models.functions import Lower
# Create your views here.
from .models import Employee, Addr, Emp, Customer, Account, Course, StudentDetails
from .models import Student
from .DButils import getEmployee

#####################################################################################################

def handleCreate1(request):
    if (request.method == 'GET'):
        return render(request, "employee.html",{})


    if (request.method == 'POST'):
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]
        password = request.POST["password"]

        # create emp obj with req data using model class
        e = Employee(firstName=firstname, lastName=lastname, age=age, username=username, password=password)
        e.save()

        return render(request, "showEmployee1.html", {"msg": "emp created"})
    return render(request, "showEmployee1.html", {"msg": "emp creation failed"})

##################################Method for student information###########################
def handleStudent1(request):
    if (request.method == 'GET'):
        return render(request, "studentForm.html",{})
    if (request.method == 'POST'):
        id = request.POST["studentId"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        rollno=request.POST["rollNo"]
        branch=request.POST["branch"]
        age = int(request.POST["age"])
        dob = request.POST["dob"]

        # create emp obj with req data using model class
        e = Student(id=id,firstName=firstname, lastName=lastname, rollNo=rollno,branch=branch,age=age,dob=dob)
        e.save()
        return render(request, "showStudent.html", {"msg": "Student created"})
    return render(request, "showStudent.html", {"msg": "Student creation failed"})

###############################################employee login###################



def handleLogin(request):
    if (request.method == 'GET'):
        return render(request, "customerLogin.html", {})

    if (request.method == 'POST'):
        # GET THE USERNAME and PASSWORDw
        username = request.POST["username"]
        password = request.POST["password"]
        # SELECT * FROM EMPLOYEE where username = <> and password =<>
        eObj=getEmployee(username,password)
        #eObj = Employee.objects.filter(username=username, password=password)

        """return render(request, "customerLogin.html", {"msg": "invalid username or password"})"""

    if (eObj):
        # case when user name and pwd is correct
        # keep the data in the sesssion
        e = eObj.first()
        request.session["id"] = e.id
        request.session["firstName"] = e.firstName
        request.session["lastName"] = e.lastName
        request.session["email"] = e.email
        request.session["username"] = e.username
        request.session["dept"] = e.dept
        return render(request, "customerMenu.html", {"msg": "login sucess"})
    else:
        username = request.POST["username"]
        # case when user name and pwd is wrong
        eObj=Employee.objects.get(username)
        for i in range(1,5):
            if eObj.count<=5:
                eObj.count=eObj.count+1
            else:
                return HttpResponse("Login Failed for many times!!")

        #return render(request, "customerLogin.html", {"msg": "invalid username"})

################emplogout####################
 #delete the session data during the logout
def handleEmpLogout(request):
        del request.session["id"]
        del request.session["fname"]
        del request.session["lname"]
        return render(request, "customerLogin.html", {"msg": "logout sucess"})


# #################### get all employee##################
def handleGetall(request):
    # select * from customer
    # all rows are converted to emp objects
    # al emp objs are stored in list
    list = Employee.objects.all()

    return render(request, "getall.html", {"emps": list})
##################Get employee by Id#############################
def handleGet(request):
    if (request.method == 'GET'):
        # click on link
        return render(request, "get.html", {})
    if (request.method == 'POST'):
        # click on serach button
        MyId = int(request.POST["id"])

        # select * from customer where id = <id>
        try:
            eObj = Employee.objects.get(id=MyId)
        except:
            return render(request, "get.html", {"msg": "invalid id"})
        else:
            return render(request, "showGet.html", {"Employee": eObj})


################### search by Username##################################
def handleGet1(request):
    if (request.method == 'GET'):
        # click on link
        return render(request, "get1.html", {})

    if (request.method == 'POST'):
        # click on serach button
        MyName = (request.POST['username'])

        eObj = None

        try:
            eObj = Employee.objects.get(username=MyName)

        except:
            return render(request, "get1.html", {"msg": "invalid name"})

        else:
            return render(request, "showGet.html", {"Employee": eObj})
###################Delete Employee#####################################
def handleDlt(request):
    if (request.method == 'GET'):
        return render(request, "dlt.html",{})

    if (request.method == 'POST'):
        MyId = int(request.POST["id"])
        eObj=None
        try:
            eObj = Employee.objects.get(id=MyId)
            eObj.delete()
        except:
            return render(request, "get.html", {"msg":"invalid id"})
        else:
            return render(request, "showDlt.html", {"msg" :"delete success"})



#update by id
def handleUpdate(request):
        MyId = int(request.GET["id"])
        eObj = Employee.objects.get(id=MyId)
        return render(request, "update.html", {"Employee":eObj})


def handleUpdate1(request):
    # capture the incoming new  data
    id = request.POST["id"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    age = int(request.POST["age"])
    username = request.POST["username"]

    # get existing data from db
    eObj = Employee.objects.get(id=id)
    eObj.firstName = firstname
    eObj.lastName = lastname
    eObj.age = age
    eObj.username = username

    eObj.save()
    return render(request, "showEmployee1.html", {"msg": "emp updated"})
#############################Sort Employee by Id##########################
def handlSortEmp(request):
    # select * from customer
    # all rows are converted to emp objects
    # al emp objs are stored in list
    list = Employee.objects.order_by(Lower('username').desc())
    return render(request, "sortEmp.html", {"emp": list})
###########################################################
def handleOnetoone(request):
    # create addr obj

    # save addres

    # create emp obj and keep add obj inside emp

    # save emp
    a = Addr(street="marath", city="bang", country="india", zip="1234")
    a.save()
    e = Emp(firstName="kumar", lastName="ram", currAddr=a)
    e.save()
    return HttpResponse("one to one success")
#####################OnttoMany##############################
def handleManytoone(request):
    #create  cust obj and save
    c= Customer(name="ramana" , age=34)
    c.save()

    # create mul accounts obj
    #every account has customer associated
    # and save every account
    a1 = Account(name="loan account", custId = c)
    a2 = Account(name="credit account", custId=c)
    a3 = Account(name="debit account", custId=c)
    a1.save()
    a2.save()
    a3.save()

    return HttpResponse("one to many/many to one success")
##################Many To Many###############################
def handleManytomany(request):
    # create student1
    s1 = Student()
    s1.name = "kumar"
    s1.mobileNo = "1223434"
    s1.save()

    # create student2
    s2 = Student()
    s2.name = "kumar1"
    s2.mobileNo = "999999"
    s2.save()

    # add s1 and s2 to course object

    c1 = Course()
    c1.courseName = "django"

    c1.save()

    c1.students.add(s1)
    c1.students.add(s2)

    c1.save()
    return HttpResponse(" many to many success")
#####################################################################
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *

# Create your views here.
"""def hotel_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = HotelForm()
	return render(request, 'uploadFile.html', {'form' : form})
"""

def success(request):
	return HttpResponse('successfully uploaded')

"""def display_hotel_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        hotels = Hotel.objects.all()
        return render(request, 'displayimage.html',{'hotel_images': hotels})"""