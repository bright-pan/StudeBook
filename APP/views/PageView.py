#StudeBook
from APP.views.MainView import MainView
#sb
from APP.models.PageModel import Page
from APP.models.PageSubscriptionModel import PageSubscription
from django.http import HttpResponse, HttpResponseRedirect
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

"""
 ### StudeBook main page ### 
 @class APPView
 @version 0.1
 @author StudeBook inc.
"""

class PageView (MainView):

    #Get pages list
    def index(self, request, page = 1) :
        userLogin = super(PageView, self).getUserLogin(request);
        if request.method == "POST":
            search = request.POST['search'];
        else:
            search = '';
        pages = Page.objects.filter((Q(publiced='1') | Q(user_id = userLogin.user)) & (Q(title__icontains = search))).order_by('title');
        
        paginator = Paginator(pages, 10);
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            pages = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            pages = paginator.page(paginator.num_pages)

        paginationRange = [i+1 for i in range(pages.paginator.num_pages)];  

        return super(PageView, self).render(request, 'page/index.html', {
            'title'   : 'All pages', 
            'paginationRange' : paginationRange,
            'page_list' : pages,
        
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
            
        return HttpResponseRedirect('/page/show/' + pageID)

    #Edit detail page 
    def deletePage(self, request, pageID) :
        page = Page.objects.get(page_id = pageID);
        userLogin = super(PageView, self).getUserLogin(request);

        if (page.user_id == userLogin.user.user_id) :
            page.delete()
            return HttpResponseRedirect('/page/')

        return HttpResponseRedirect('/page/show/' + pageID)

    def create(self, request) :
        userLogin = super(PageView, self).getUserLogin(request)
        new_entry = Page(title='title', user=userLogin.user, body='body', publiced='1')
        new_entry.save()

        return HttpResponseRedirect('/page/show/'+ str(new_entry.page_id) +'/edit/')

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
        return HttpResponseRedirect('/page/show/' + pageID)
    
    def subscribe (self, request, pageID) :
        userLogin = super(PageView, self).getUserLogin(request);
        pagesubscription = PageSubscription(page_id = pageID, user_id = userLogin.user.user_id)
        pagesubscription.save()

        return HttpResponseRedirect('/page/show/' + pageID)
