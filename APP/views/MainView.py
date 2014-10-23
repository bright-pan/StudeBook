#DJANGO
from django.views.generic import View
from django.shortcuts import render

"""
 @class MainView
 @version 0.1
 @author StudeBook inc.
"""

class MainView(View):
    
    def render (self, request, template, params) :
        #Manipulate params
        params.update({ 'test' : 404 });
        #Render view
        return render(request, template, params);
    