from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from Character_Generator import views

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^index$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^generate/(?P<region>\w+)$', views.generate_view, name='generate'),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    url(r'^.*', TemplateView.as_view(template_name='joke.html'), name='home')
)
