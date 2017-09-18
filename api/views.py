from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

# Create your views here.

class UsersView(View):
    def post(self, request):
        return HttpResponse("Not Implemented")

class UserView(View):
    def put(self, request):
        return HttpResponse("Not Implemented")

    def delete(self, request):
        return HttpResponse("Not Implemented")

    def get(self, request):
        return HttpResponse("Not Implemented")


class AuthView(View):
    def post(self, request):
        return HttpResponse("Not Implemented")

class LocationsView(View):
    def post(self, request):
        return HttpResponse("Not Implemented")

    def get(self, request):
        return HttpResponse("Not Implemented")





