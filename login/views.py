
# Create your views here.
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.shortcuts import render
import csv
import re

from .forms import UserForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def ex1(request):
    res = "<font color='red'>welcome to django</font>"
    return HttpResponse(res)
def handleHello(request):
    return render(request, "helloResponse.html", {})
def handleResponseData(request):
    return render(request, "showResponse.html", {"data":"hi How Are You "})
def handleMultipleResponse(request):
    responseData = {"userName":"kumar","id":101,"salary":23900.089}
    return render(request, "showMultiResponse.html", responseData)

###################################Sending Object####################################
class Person:
    id = None
    name = None
    age = None
    pancard = None


# handleShow1 has to send the person object to the "showRes1.html"
def handleShow1(request):
    p = Person()


    p.id = 2000
    p.name = "kumar"
    p.age = 34
    p.pancard = "CNVPD2557D"

    return render(request, "showRes1.html", {"pData": p})

########################################Has a Relation#########################################################
class Address:
    hno = None
    city = None
    state = None
    country = None
    pin = None


class StudentInfo:
    firstName = None
    lastName = None
    addr = None


"""
create Address obj with data
create StudentInfo obj with data
keep Address obj inside the StudentInfo obj
Send StudentInfo obj  to the "showRes2.html".
showRes2.html :-> print both StudentInfo and Address
"""


def handleShow2(request):
    # create address obj
    a = Address()
    a.hno = "#23"
    a.city = "hyd"
    a.state = "KA"
    a.country = "IN"
    a.pin = 1234

    # create student obj
    stu = StudentInfo()
    stu.firstName = "ram"
    stu.lastName = "sharma"

    # keep address obj inside student
    stu.addr = a

    return render(request, "showRes2.html", {"sObj": stu})
##############################Sending List#########################
#lists of strings
def handleShow3(request):
  myCities = ["hyd","bangalore","chennai","kolkatta","pune","maduari"]
  return render(request, "showRes3.html", {"cities": myCities})

#################Sending list of Objects#####################################
# handleShow5 has to return the list of person obj to the "showRes5.html"
def handleShow5(request):
    p1 = Person()
    p1.id = 2000
    p1.name = "kumar"
    p1.age = 34

    p2 = Person()
    p2.id = 2001
    p2.name = "ram"
    p2.age = 35

    p3 = Person()
    p3.id = 2002
    p3.name = "murthy"
    p3.age = 29

    list = [p1, p2, p3]  # add p1,p2 to the list
    return render(request, "showRes5.html", {"persons": list})
 ##################IF statement################################
def handleShow7(request):
    return render(request, "showRes7.html", {"status": 1})

###################Assignment#################################################
"""Req:
Send list of Student with address objs to the template.
every Student obj has address obj.
if there are no studnts then display :-> "No students "
if there is no address for studnt then display :-> "No address available "
"""
class StudentAddress:
    hno = None
    city = None
    state = None
    country = None
    pin = None


class StudentInformation:
    firstName = None
    lastName = None
    addr = None

class Nodetails:
    studentDetails="No Student Details Found"
    studentAddress="No Address found for this student"


"""
create Address obj with data
create StudentInfo obj with data
keep Address obj inside the StudentInfo obj
Send StudentInfo obj  to the "showRes2.html".
showRes2.html :-> print both StudentInfo and Address
"""


def handleShow8(request):
    # create address obj
    a1 = StudentAddress()
    a1.hno = "#23"
    a1.city = "hyd"
    a1.state = "KA"
    a1.country = "IN"
    a1.pin = 1234

    a2 = StudentAddress()
    a2.hno = "#24"
    a2.city = "Beng"
    a2.state = "KA"
    a2.country = "IN"
    a2.pin = 12345

    a3 = StudentAddress()

    a4 = StudentAddress()
    a4.hno = "#24"
    a4.city = "Mysore"
    a4.state = "KA"
    a4.country = "IN"
    a4.pin = 1357
    # create student obj
    stu1 = StudentInformation()
    stu1.firstName = "ram"
    stu1.lastName = "sharma"

    stu2 = StudentInformation()
    stu2.firstName = "Sri"
    stu2.lastName = "Ram"

    stu3 = StudentInformation()
    stu3.firstName = "chetan"
    stu3.lastName = "Rishwaa"

    stu4 = StudentInformation()

    # keep address obj inside student
    stu1.addr = a1
    stu2.addr = a2
    stu3.addr=a3
    stu4.addr= a4
    list=[stu1,stu2,stu3,stu4]
    return render(request, "showRes8.html", {"sObj": list})

###############################################Assignment display Information when details not found#####################
class StudentAddress:
    hno = None
    city = None
    state = None
    country = None
    pin = None


class StudentInformation:
    firstName = None
    lastName = None
    addr = None

def handleShow9(request):
    # create address obj
    a1 = StudentAddress()
    a1.hno = "#23"
    a1.city = "hyd"
    a1.state = "KA"
    a1.country = "IN"
    a1.pin = 1234

    a2 = StudentAddress()
    a2.hno = "#24"
    a2.city = "Beng"
    a2.state = "KA"
    a2.country = "IN"
    a2.pin = 12345

    a3 = StudentAddress()

    a4 = StudentAddress()
    a4.hno = "#24"
    a4.city = "Mysore"
    a4.state = "KA"
    a4.country = "IN"
    a4.pin = 1357
    # create student obj
    stu1 = StudentInformation()
    stu1.firstName = "ram"
    stu1.lastName = "sharma"

    stu2 = StudentInformation()
    stu2.firstName = "Sri"
    stu2.lastName = "Ram"

    stu3 = StudentInformation()
    stu3.firstName = "chetan"
    stu3.lastName = "Rishwaa"

    stu4 = StudentInformation()
    stu4.firstName= 0
    stu4.lastName=0
    stu4 = StudentInformation()


    # keep address obj inside student
    stu1.addr = a1
    stu2.addr = a2
    stu3.addr=a3
    stu4.addr= a4
    list=[stu1,stu2,stu3,stu4]
    return render(request, "showRes9.html", {"sObj": list})
###################################Student has multiple Addresses#################################

class Address:
    hno = None
    city = None
    state = None
    country = None
    pin = None


class Student:
    firstName = None
    lastName = None
    addr = None

def handleShow10(request):
    # create address obj
    a1 = Address()
    a1.hno = "#23"
    a1.city = "hyd"
    a1.state = "KA"
    a1.country = "IN"
    a1.pin = 1234

    a2 = Address()
    a2.hno = "#24"
    a2.city = "Beng"
    a2.state = "KA"
    a2.country = "IN"
    a2.pin = 12345

    a3 = Address()
    a3.hno = "#24"
    a3.city = "Mysore"
    a3.state = "KA"
    a3.country = "IN"
    a3.pin = 1357
    # create student obj
    stu1 = Student()
    stu1.firstName = "Sri"
    stu1.lastName = "Ram"
    # keep address obj inside student
    stu1.addr = [a1,a2,a3]
    return render(request, "showRes10.html", {"sObj":stu1})


##################################Backend Validate Assignment 26/11/2020###########################

def handleValidate1(request):
    return render(request, "validate1.html", {"status": 1})


def validation1(request):
    userName=request.GET["userName"]
    emailId=request.GET["email"]
    password=request.GET["password"]
    confirmPassword=request.GET["confirmPassword"]

    emailPattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    passwordPattern = r'[A-Za-z0-9@#$%^&+=]{8,}'

###########Combined validation of form fields --if they are correct ,displays succes message#####################
    if userName=="admin" and (re.search(emailPattern,emailId)) and (re.fullmatch(passwordPattern, password)) and confirmPassword==password:
        return successMethod(request)
##############user name errors when empty and invalid##################
    if len(userName) == 0:
        userInfo=" User Name is Empty !!"
    elif userName !="admin":
         userInfo="Invalid User "
    else:
        userInfo = "  "
##############email Id errors when empty and invalid##################
    if len(emailId) ==0:
        emailInfo="Email Id is Empty!!"
    elif not (re.search(emailPattern,emailId)):
        emailInfo="InValid Email"
    else:
        emailInfo=" "

##############password errors when empty and invalid##################

    if len(password) == 0:
        passwordInfo="Please give password"
    elif re.fullmatch(passwordPattern, password):
        passwordInfo=" "
    else:
        passwordInfo = "InValid Password "


##############confirm password errors when empty and invalid##################

    if password and len(confirmPassword) ==0:
        confirmPasswordInfo = "confirm password should not be empty"
    elif confirmPassword and len(password)==0:
        confirmPasswordInfo="Please enter a password before confirming !!"
    elif confirmPassword== password:
        confirmPasswordInfo=" "

    else:
        confirmPasswordInfo="Password did not Match !"
################Array of in errors information of fields########################
    result=[userInfo,emailInfo,passwordInfo,confirmPasswordInfo]

    return render(request, "validate1.html", {"validity":result})

#########################Success Message page method##################
def successMethod(request):
        return render(request,"validationResult.html",{"result":"Registration Success!"})
#################################homepage################################################

def handleIndex(request):
    return render(request, "index.html", )
##################################Submit form#######################################
def handlePostRequest(request):
    return render(request, "requestPost.html")
#method when customer clicks on "requestPost" click
def handleSubmitPost(request):
    name = request.POST["name"]
    age = int(request.POST["age"])
    return render(request, "showRes11.html", {"msg": "hi from POST ", "myName": name, "myAge": age})
###################identify get & post######################################

#method when customer clicks on "GetAndPost" click
def showRequestGetAndPost(request):
    return render(request, "requestGetAndPost.html")

#handle both post and get when customer clicks on Button
def handleRequestGetAndPost(request):
    if(request.method == 'GET'):
        name= request.GET["name"]
        age = int(request.GET["age"])
        return render(request, "showRes11.html", {"msg" : "hi from GET " ,"myName" : name , "myAge" : age})

    if (request.method == 'POST'):
        name = request.POST["name"]
        age = int(request.POST["age"])
        return render(request, "showRes11.html", {"msg" : "hi from POST " ,"myName": name, "myAge": age})

######################download pdf and save############################

def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 26)
    p.drawString(100,700, "Hello user this is your statement")
    p.drawString(200,900, "see you soon.....")
    p.showPage()
    p.save()
    return response
#############################download csv file###########################

def getCsv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emps.csv"'

	  #generate the csv obj
    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'age','sal'])
    writer.writerow(['101', 'user1', 28, 1000])
    writer.writerow(['102', 'user2', 29, 1200])
    writer.writerow(['103', 'user3', 30, 1300])

    return response
############################Set and get Cookies############################
#method will set the cookie ad add cookie to response
def handleSetCookie(request):
    response = HttpResponse("Added cookie")
    response.set_cookie('MyCookie', 'KRISHNA DJANGO')
    return response
# method to get the cookie value from the request
def handleGetCookie(request):
    myCookie = request.COOKIES['MyCookie']
    return HttpResponse("showing cookie COOKIE VALUE =  " + myCookie)
#method to delete coookie
def handleDeleteCookie(request):
    response = HttpResponse("deleted cookie")
    response.delete_cookie('MyCookie')
    return response
###############################Login ####################################################################

def showLogin(request):
    return render(request, "customerLogin.html")


def handleLogin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    if username == 'admin' and password == 'admin':
        return render(request, "showLoginResponse.html", {"msg": " login sucess"})
    else:
        return render(request, "showLoginResponse.html", {"msg": " login failure"})

#############################form submission and retaining data along with error message#############
def handleShowStudentForm(request):
    return render(request, "showStudentForm.html")
def handleSubmitStudentForm(request):
    firstName=request.POST.get("firstName")
    lastName=request.POST.get("lastName")
    sem=int(request.POST.get("sem"))
    branch=request.POST.get("branch")
    studentInfo=[firstName,lastName,sem,branch]
    if ((len(firstName)>8 and len(firstName)<15)) and (sem>=1 and sem<=8) and (branch=="cse" or branch=="ece" or branch=="mech" or branch=="civil"):
        return render(request, "submitStudentForm.html", {"msg":"Success!! Data Saved"})
    else:
        return render(request, "submitStudentForm.html", {"msg":"Submit Failed!!","sInfo":studentInfo})

#################################################################################################
class RegisterInfo:

     def __init__(self,firstname,lastname,age,username,password):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            self.username = username
            self.password = password


def handleRegister(request):
    if (request.method == 'GET'):
        # when  customer clicks on register link
        return render(request, "register.html", {})

    if (request.method == 'POST'):
        # when  customer clicks on register button

        # capture the request data

        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        age = int(request.POST["age"])
        username = request.POST["username"]
        password = request.POST["password"]

        # keep the data in RegisterInfo object
        info = RegisterInfo(firstname, lastname, age, username, password)

        # in the request data is wrong then send erorr message and info object to the register.html

        if len(firstname) < 8:
            return render(request, "register.html", {"msg": " firstname has to be min 8 char", "info": info})

        if len(lastname) < 6:
            return render(request, "register.html", {"msg": " lastname has to be min 6 char", "info": info})

        if (age) not in range(18, 60):
            return render(request, "register.html", {"msg": " age has to be in 18-60", "info": info})

        if len(username) < 5:
            return render(request, "register.html", {"msg": " username has to be min 5 char", "info": info})

        if len(password) not in range(8, 12):
            return render(request, "register.html", {"msg": " password has to be in  8-12 char", "info": info})

        return render(request, "success.html", {"msg": " Registation sucess...."})

    return HttpResponse("matching handler not found")
##########################################################################################

def handleForm1(request):
    form = UserForm()
    return render(request, "form1.html", {"form": form})


def handleForm2(request):
    form = UserForm(request.POST)
    if form.is_valid():
        fname = form.cleaned_data['fname']
        lname = form.cleaned_data['lname']
        address = form.cleaned_data['address']
        email = form.cleaned_data['email']
        return render(request, "response1.html", {"fname": fname, "lname": lname, "address": address, "email": email})
    else:
        return render(request, "form1.html", {"form": form})
###############################################################################################
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def hotel_image_view(request):

	if request.method == 'POST':
		form = HotelForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = HotelForm()
	return render(request, 'hotel_image_form.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')



"""def imageUpload(request):
    if request.method == 'POST':
        form = AgentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AgentForm()
    return render(request, 'uploadImage.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
"""


