import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import Employee
from .serializers import EmpSerialize


class EmpViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()  # what to retrive
    serializer_class = EmpSerialize  # which should obj holds the response


from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth.models import User


@api_view(["GET"])
@csrf_exempt
def get_users(request):
    # get the data
    users = User.objects.all()

    # wrap to serializer
    serializer = UserSerializer(users, many=True, context={
        'request': request,
    })

    # add to json response
    return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
def add_user(request):
    # get the json obj from request json
    payload = json.loads(request.body)
    # create the model and save
    user = User.objects.create_user(
        username=payload["username"], password=payload["password"], email=payload["email"],
        first_name=payload["firstName"], last_name=payload["lastName"])

    return JsonResponse({"status": "user created"}, safe=False, status=status.HTTP_201_CREATED)
