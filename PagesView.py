#StudeBook
from APP.views.MainView import MainView
#sb
from APP.models.PageModel import Page
"""
 ### StudeBook main page ### 
 @class APPView
 @version 0.1
 @author StudeBook inc.
"""

class PagesView (MainView):

    def get (self, request) :
        
    	pages = Page.objects.all().order_by('title');

        return super(PagesView, self).render(request, 'pages.html', {
            'title'   : 'All Pages', 
            'page_list' : pages

        });

