#StudeBook
from APP.views.MainView import MainView
#sb
from APP.models.PageModel import Page
from APP.models.PageSubscriptionModel import PageSubscription
from django.http import HttpResponse, HttpResponseRedirect
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User
from django.db.models import Q

"""
 ### StudeBook main page ### 
 @class APPView
 @version 0.1
 @author StudeBook inc.
"""

class PageView (MainView):

    #Get pages list
    def index(self, request) :
        userLogin = super(PageView, self).getUserLogin(request);
        if request.method == "POST":
            search = request.POST['search'];
        else:
            search = '';
        
        return super(PageView, self).render(request, 'page/index.html', {
            'title'   : 'All pages', 
            'page_list' : Page.objects.filter((Q(publiced='1') | Q(user_id = userLogin.user)) & (Q(title__contains = search))).order_by('title'),
        
        });

    #Get detail page 
    def show(self, request, pageID) :
        try :
            page = Page.objects.get(page_id = pageID);
            userLogin = super(PageView, self).getUserLogin(request);
            members = PageSubscription.objects.filter(page = page);
            member = PageSubscription.objects.filter(Q(page = page) & Q(user_id = userLogin.user));

            return super(PageView, self).render(request, 'page/show.html', {
                'title' : 'page : ' + pageID,
                'page' : page,
                'members' : members,
                'member' : member,
            });
        except :
            return HttpResponseRedirect('/page/')

    #Edit detail page 
    def updatePage(self, request, pageID) :
        page = Page.objects.get(page_id = pageID);
        userLogin = super(PageView, self).getUserLogin(request);

        if (page.user_id == userLogin.user.user_id) :

            return super(PageView, self).render(request, 'page/update.html', {
                'title' : pageID,
                'test' : userLogin.user.user_id,
                'page' : page,
            });
            
        return HttpResponseRedirect('/page/getPage/' + pageID)

    #Edit detail page 
    def deletePage(self, request, pageID) :
        page = Page.objects.get(page_id = pageID);
        userLogin = super(PageView, self).getUserLogin(request);

        if (page.user_id == userLogin.user.user_id) :
            page.delete()
            return HttpResponseRedirect('/page/')

        return HttpResponseRedirect('/page/getPage/' + pageID)

    def create(self, request) :
        userLogin = super(PageView, self).getUserLogin(request)
        new_entry = Page(title='title', user=userLogin.user, body='body', publiced='0')
        new_entry.save()

        return HttpResponseRedirect('/page/getPage/'+ str(new_entry.page_id) +'/edit/')

    def update (self, request) :
        name = request.POST.get('name', '')
        value = request.POST.get('value', '')
        pk = request.POST.get('pk', '')

        record = Page.objects.get(page_id = pk)
        record.__setattr__(name, value)
        record.save()

        return super(PageView, self).render(request, 'page/update.html', {
            
        });

    def unsubscribe (self, request, pageID) :
        userLogin = super(PageView, self).getUserLogin(request);
        subscription = PageSubscription.objects.filter(Q(page_id = pageID) & Q(user_id = userLogin));

        subscription.delete()
        return HttpResponseRedirect('/page/getPage/' + pageID)
    
    def subscribe (self, request, pageID) :
        userLogin = super(PageView, self).getUserLogin(request);
        pagesubscription = PageSubscription(page_id = pageID, user_id = userLogin.user.user_id)
        pagesubscription.save()

        return HttpResponseRedirect('/page/getPage/' + pageID)
