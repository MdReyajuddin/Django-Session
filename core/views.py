from django.shortcuts import render
from django.http import HttpResponse

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Reyaj</h1>")
def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Reyaj<br> cookie createed")
    else:
        response = HttpResponse("Reyaj <br> Your browser doesnot accept cookies")
    return response


def create_session(request):
    request.session['username']= 'reyaj'
    request.session['password']= 'reyaj786'

    return HttpResponse('session created')

def access_session(request):
    response ={}
    if request.session.get('username'):
        username = request.session.get('username')
        response['username']= username
    if request.session.get('password'):
        password = request.session.get('password')
        response['password'] = password

    return render(request, 'home.html', {'response': response})

