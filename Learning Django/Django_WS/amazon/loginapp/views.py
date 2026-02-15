from django.shortcuts import render, HttpResponse

def login_view(request):
    print("Welcome")
    return HttpResponse("Welcome")
