from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.context import RequestContext
from seal.model.delivery import Delivery
from seal.view import HTTP_401_UNAUTHORIZED_RESPONSE
from seal.model.course import Course
#from auto_correction.automatic_correction_runner import AutomaticCorrectionRunner

#@login_required
#def run_automatic_correction_subprocess(request):
#    runner = AutomaticCorrectionRunner()
#    results = runner.run()
#    return render(request, 'automatic_correction/results.html', {'results': results}, 
#                  context_instance=RequestContext(request))

@login_required
def details(request, idcourse, iddelivery):
    if(len(request.user.teacher_set.all()) > 0): # if an authenticated user "accidentally" access this section, he doesn't get an exception
        current_course = Course.objects.get(pk = idcourse)
        courses = Course.objects.all()
        
        delivery = Delivery.objects.get(pk=iddelivery)
        automatic_correction = delivery.get_automatic_correction()
        return render(request, 'automatic_correction/details.html',
                      {'current_course': current_course,
                       'courses': courses,
                       'automatic_correction': automatic_correction, 'practice': delivery.practice},
                      context_instance=RequestContext(request))
    else:
        return HTTP_401_UNAUTHORIZED_RESPONSE
    
