
from django.http import HttpResponse
from django.views.generic import View
import json

"""
 ### StudeBook main api page ### 
 @class APIView
 @version 0.1
 @author StudeBook inc.
"""

class APIView (View):
    
    #Main page
    def get (self, request) :        
        #Render json
        data = json.dumps({ 'status' : 200, 'message' : 'StudeBook API' });
        return HttpResponse(data,content_type='application/json');