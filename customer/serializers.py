from rest_framework import serializers

from .models import Employee
from django.contrib.auth.models import User, Group

class EmpSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
         model = Employee
         fields = ['id' ,'firstName' ,'lastName', 'age', 'username']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password','email', 'first_name','last_name','groups']





