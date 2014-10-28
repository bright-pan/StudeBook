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

class PageView (MainView):

    def get (self, request, pageID) :
        
    	page = Page.objects.get(page_id = pageID);

        return super(PageView, self).render(request, 'page.html', {
            'page' : page
        });

