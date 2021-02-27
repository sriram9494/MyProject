from django.urls import path
from . import views
urlpatterns = [
    path('ex1/', views.ex1,name="ex1 page"),
    path('hello/', views.handleHello,name="ex1 page"),
    path('responseData/', views.handleResponseData,name="ex1 page"),
    path('responseMultiData/', views.handleMultipleResponse,name="response-MultiData"),
    path('show1/', views.handleShow1, name="show1-page"),
    path('show2/', views.handleShow2, name="show2-page"),
    path('show3/', views.handleShow3, name="show3 page"),
    path('show5/', views.handleShow5, name="show5 page"),
    path('show7/', views.handleShow7, name="IF-page"),
    path('show8/', views.handleShow8, name="show8-page"),
    path('show9/', views.handleShow9, name="show9-page"),
    path('show10/', views.handleShow10, name="show10-page"),
    path('validate1/', views.handleValidate1, name="myValidation"),
    path('validate1/validation1/', views.validation1, name="validation1"),
    path('validate1/validation1/', views.successMethod, name="validation1"),
    #path('', views.handleIndex,name="index page"),
    path('requestPost/', views.handlePostRequest, name="request11-page"),
    path('submitPost/', views.handleSubmitPost, name="submitPost-page"),
    path('requestGetAndPost/', views.showRequestGetAndPost, name="requestPost-page"),
    path('submitRequestGetAndPost/', views.handleRequestGetAndPost, name="requestPost-page"),
    path('pdf/', views.getpdf, name="pdf-page"),
    path('csv/', views.getCsv, name="csv-page"),
    path('setcookie/', views.handleSetCookie, name="setcookie-page"),
    path('getcookie/', views.handleGetCookie, name="getcookie-page"),
    path('deletecookie/', views.handleDeleteCookie, name="deletecookie-page"),
    path('showLogin/', views.showLogin, name="login-page"),
    path('submitLogin/', views.handleLogin, name="submit-Login"),
    path('showStudentForm/', views.handleShowStudentForm, name="show-form"),
    path('submitStudentForm/', views.handleSubmitStudentForm, name="submit-form"),
    path('register/', views.handleRegister, name="register-page"),
    path('form1/', views.handleForm1, name="form-page"),
    path('processForm1/', views.handleForm2, name="processForm1-page"),


]
