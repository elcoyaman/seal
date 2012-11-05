from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Index page. DO NOT TOUCH
urlpatterns = patterns('view.home',
    url(r'^/?$', 'index'),
)

urlpatterns += patterns('view.delivery',
    url(r'^delivery/newdelivery/(?P<idpractice>\d+)/(?P<idstudent>\d+)?/$', 'newdelivery'),
)

urlpatterns += patterns('view.practice',
    url(r'^practices/?$', 'index'),
    url(r'^practices/newpractice/(?P<idcourse>\d+)$', 'newpractice'),
    url(r'^practices/editpractice/(?P<idcourse>\d+)/(?P<idpractice>\d+)/$', 'editpractice'),
    url(r'^practices/download/(?P<idpractice>\d+)/$', 'download')
)

urlpatterns += patterns('view.student',
    url(r'^students/?$', 'index'),
    url(r'^students/home/(?P<idstudent>\d+)$', 'home'),
    url(r'^students/newstudent/(?P<idcourse>\d+)$', 'newstudent'),
    url(r'^students/editstudent/(?P<idcourse>\d+)/(?P<idstudent>\d+)/$', 'editstudent'),
    url(r'^students/practicelist/(?P<idcourse>\d+)/(?P<idstudent>\d+)/$', 'practicelist'),
)

urlpatterns += patterns('view.course',
    url(r'^course/?$', 'index'),
    url(r'^course/newcourse/?$', 'newcourse'),
    url(r'^course/editcourse/(?P<idcourse>\d+)$', 'editcourse'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
