from django.shortcuts import render
from django.views.generic.base import TemplateView



class testpage(TemplateView) :
    template_name ="test.html"


    

    def get_context_data(self, **kwargs):
       context = super(TemplateView, self).get_context_data(**kwargs)
       # here's the difference:
       x=25*562121
       y=x/2
       context['yvalue'] = y
       return context








class homepage(TemplateView) :
    template_name ="home.html"