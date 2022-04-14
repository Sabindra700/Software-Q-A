from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PersonForm
#import requests

from subprocess import run, PIPE
import sys

def person(request):
    form=PersonForm
    if request.method == 'POST':
        personForm = PersonForm(request.POST)
        if personForm.is_valid():
            personForm.save()
            messages.success(request, 'Form is Submitted.')
            redirect('/myweb/person')
            return redirect('/myweb')
    return render(request, 'person.html', {'form':form})

def index(request):
    template = loader.get_template('mydoc.html')
    return HttpResponse(template.render())

def button(request):
    return render(request,'mydoc.html')

#def output(request):
    #data = requests.get('//Users//sabin//Desktop//djangoProject//myweb//tests.py')
    #print(data.text)
    #data=data.text
    #return render(request, 'mydoc.html', {'data' :data})

def external(request):
    out = run([sys.executable,'tests.py'], stdout=PIPE)
    print(out)

    return render(request,'mydoc.html',{'data1' :out.stdout})