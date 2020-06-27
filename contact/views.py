from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# def contactView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['ch.karavelas@hotmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "contact.html", {'form': form})

def contactView(request):
    mapbox_access_token = 'pk.eyJ1IjoiY2hyaXNrYXJhdmVsIiwiYSI6ImNrYjI1cWxmMTA4cncycXM1dDA3eHM1azcifQ.0BArPTUD-DItjqVgkBfk_Q'
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'contact.html', 
                  { 'mapbox_access_token': mapbox_access_token })
    else:
        subject=request.POST['subject']
        message=request.POST['message']
        from_email=request.POST['from_email']
        try:
            send_mail(subject, message, from_email, ['ch.karavelas@hotmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render(request, "contact.html",  { 'mapbox_access_token': mapbox_access_token })
    return render(request, "contact.html", {'form': form, })


                  
def successView(request):
    return HttpResponse('Success! Thank you for your message.')