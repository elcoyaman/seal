'''
Created on 28/10/2012

@author: martin
'''
from django.http import HttpResponseRedirect
from seal.forms.course import CourseForm
from django.shortcuts import render_to_response, render
from seal.model.course import Course
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.context import RequestContext

def index(request):
    courses_list = Course.objects.all().order_by('-name')
    paginator = Paginator(courses_list, 25) # Show 25 courses per page
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        courses = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        courses = paginator.page(paginator.num_pages)
    return render_to_response('course/index.html', {"courses": courses}, context_instance=RequestContext(request))

def newcourse(request):
    if (request.method=='POST'):
        form = CourseForm(request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect('/course')
    else:
        form = CourseForm()
    return render(request,'course/newcourse.html',{'form': form,})
