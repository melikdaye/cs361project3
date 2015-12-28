from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from formapp.forms import teacherform, studentform, courseform
from formapp.models import teachers, courses, students


def addteacher(request):
    if request.method == 'POST':
        form = teacherform(request.POST)
        if form.is_valid():
            form.save_teacher()
            return HttpResponseRedirect('/teachersuccess')
    else:
        form = teacherform()
    return render_to_response('teacherform.html', {'form': form},
                                      RequestContext(request))

def addstudent(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save_student()
            return HttpResponseRedirect('/studentssuccess')
    else:
        form = studentform()
    return render_to_response('studentform.html', {'form': form,},
                                      RequestContext(request))

def addcourse(request):
    if request.method == 'POST':
        form = courseform(request.POST)
        if form.is_valid():
            form.save_course()
            return HttpResponseRedirect('/coursesuccess')
    else:
        form = courseform()
    return render_to_response('courseform.html', {'form': form},
                                      RequestContext(request))


def succesteacher(request):
    a=teachers.objects.all()
    return render_to_response('teachersuccess.html',{'teacher':a},RequestContext(request))
def home(request):
    return render_to_response('home.html',RequestContext(request))

def succescourse(request):
    a=courses.objects.all()
    return render_to_response('coursesuccess.html',{'course':a},RequestContext(request))

def successtudent(request):
    a=students.objects.all()

    return render_to_response('studentssuccess.html',{'student':a},RequestContext(request))

