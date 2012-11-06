from behave import *
from selenium import webdriver
from seal.model import Course, Practice
from seal.model.student import Student
from django.template.defaulttags import now
from django.contrib.auth.models import User



@given('I have opened the browser for "{url}"')
def step(context, url):
    context.browser = webdriver.Firefox()
    context.browser.get(url)

@given('I log in as "{usr}" "{passwd}"')
def step(context, usr, passwd):
    form = context.browser.find_element_by_tag_name('form')
    form.find_element_by_name('username').send_keys(usr)
    form.find_element_by_name('password').send_keys(passwd)
    form.submit()

@given('I am in the index page')
def step(context):
    print(context)
    context.browser.get('http://localhost:8000/')

@given('I am in the practice list page')
def step(context):
    print(context)
    context.browser.get('http://localhost:8000/practices/')

@given('I am at the new student form')
def step(context):
    context.browser.get('http://localhost:8000/students/newstudent')

@given('there are no courses')
def step(context):
    Course.objects.all().delete()

@given('there are no practices')
def step(context):
    Practice.objects.all().delete()

@given('there are no students')
def step(context):
    Student.objects.all().delete()

@given('course "{course}" exists')
def step(context,course):
    c = Course.objects.get_or_create(name=course)

@given('student "{name}" exists in course "{course}"')
def step(context,name, course):
    course = Course.objects.get(name=course)
    student = Student.objects.get(name=name)
    student.courses.add(course)

@given('student "{name}" does not exist in course "{course}"')
def step(context,name, course):
    course = Course.objects.get(name=course)
    if(course.student_set.filter(uid=name).exists()):
        course.student_set.remove(uid=name)

@given('there are no student in "{course}"')
def step(context, course):
    c = Course.objects.get(name=course)
    studnets = c.student_set.all()
    for student in studnets:
        student.delete()

@given('there are no practices in course "{course}"')
def step(context, course):
    c = Course.objects.get(name=course)
    practices = c.practice_set.all()
    for practice in practices:
        practice.delete()
        
@given('practice "{practice_uid}" exists in course "{course_name}" with deadline "{dead_line}"')
def step (context, practice_uid, course_name, dead_line):
    c = Course.objects.get(name=course_name)
    #deadline = dateutil.parser.parse(dead_line)
    practice = Practice.objects.get_or_create(uid=practice_uid, deadline = dead_line, file='test_file.pdf',course=c)
                
@given('I am at the new practice form for course "{namecourse}"')
def step(context,namecourse):
    c = Course.objects.get(name=namecourse)
    path = "http://localhost:8000/practices/newpractice/"+str(c.pk)
    context.browser.get(path)

@given('I am not logged in')
def step(context):
    assert True

@given('user "{uid}" is not registered')
def step(context, uid):
    if(Student.objects.filter(uid=uid).exists()):
        student = Student.objects.get(uid=uid)
        student.user.delete()
        student.delete()

@given('user "{uid}" is registered')
def step(context, uid):
    if(not(Student.objects.filter(uid=uid).exists())):
        if(User.objects.filter(username=uid).exists()):
            User.objects.get(username=uid).delete()
        user = User()
        user.username = uid
        user.set_password("seal")
        user.email = "foo@foo.foo"
        user.save()
        student = Student()
        student.user = user
        student.name = uid
        student.uid = uid
        student.email = "foo@foo.foo"
        student.save()
