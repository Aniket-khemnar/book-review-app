from django.shortcuts import render
 from django.http import HttpResponse

def home(request):
    return render(request , "login.html")

# This is function Type
'''
def home(request):
    return HttpResponse("Hey i am a Django server.")
    '''

