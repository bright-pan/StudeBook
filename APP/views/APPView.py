#StudeBook
from APP.views.MainView import MainView

"""
 ### StudeBook main page ### 
 @class APPView
 @version 0.1
 @author StudeBook inc.
"""

class APPView (MainView):

    def get (self, request) :
        
        return super(APPView, self).render(request, 'home/app.html', {
            'title'   : 'StudeBook',
            'message' : 'APPPPPPPP.'
        });