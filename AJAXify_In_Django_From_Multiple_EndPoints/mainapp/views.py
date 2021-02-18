from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Endpoint 1 for form
def form_ajax(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        if firstname and lastname:
            response = {
                 'msg':'Message from Point 1: Form has been successfully submitted',
                 'firstname': firstname,
                 'lastname': lastname
            }
            return JsonResponse(response)

# Endpoint 2 for message
def message_ajax(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname', None)
        lastname = request.POST.get('lastname', None)
        send = "Message from Point 2: "+firstname+" "+lastname+" you have successfully submitted the form!!!"
        return HttpResponse(send)

