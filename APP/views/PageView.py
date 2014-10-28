#StudeBook
from APP.views.MainView import MainView
#sb
from APP.models.PageModel import Page
from django.http import HttpResponse

"""
 ### StudeBook main page ### 
 @class APPView
 @version 0.1
 @author StudeBook inc.
"""

class PageView (MainView):

    #Get pages list
    def getPages (self, request) :
        return super(PageView, self).render(request, 'page/pages.html', {
            'title'   : 'All pages', 
            'page_list' : Page.objects.all().order_by('title')
        });
       
    #Get detail page 
    def getPage(self, request, pageID) :
        return super(PageView, self).render(request, 'page/page.html', {
            'title' : 'page : ' + pageID,
            'page' : Page.objects.get(page_id = pageID)
        });

    #Edit detail page 
    def editPage(self, request, pageID) :
        page = Page.objects.get(page_id = pageID);
        userLogin = super(PageView, self).getUserLogin(request);
        return super(PageView, self).render(request, 'page/edit.html', {
            'title' : 'page : ' + pageID,
            'test' : userLogin.user.user_id,
            'page' : page,
        });
