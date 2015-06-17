"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime

def artists(request):
    return HttpResponse('<html><head><title>Hello, Django!</title></head><body><h1>Hello, Django</h1></body></html>');

def artistdetails(request, name):
    output = '<html><head><title>' + name
    output += '</title></head><body><h1>' + name
    output += '</h1></body></html>'
    return HttpResponse(output);

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
