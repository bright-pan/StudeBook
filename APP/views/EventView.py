#StudeBook
from APP.views.MainView import MainView
#sb
from APP.models.EventModel import Event
from APP.models.EventSubscriptionModel import EventSubscription
from django.http import HttpResponse, HttpResponseRedirect
from APP.models.UserLoginModel import UserLogin
from APP.models.UserModel import User
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
"""
 ### StudeBook main event ### 
 @class APPView
 @version 0.1
 @author StudeBook inc.
"""

class EventView (MainView):

    #Get event list
    def index(self, request, page = 1) :
        userLogin = super(EventView, self).getUserLogin(request);
        if request.method == "POST":
            search = request.POST['search'];
        else:
            search = '';
        
        events = Event.objects.filter((Q(publiced='1') | Q(user_id = userLogin.user)) & (Q(title__icontains = search))).order_by('title');

        paginator = Paginator(events, 5);
        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            events = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            events = paginator.page(paginator.num_pages)

        paginationRange = [i+1 for i in range(events.paginator.num_pages)];  

        return super(EventView, self).render(request, 'event/index.html', {
            'title'   : 'All events', 
            'paginationRange' : paginationRange,
            'event_list' : events,
        
        });

    #Get detail event 
    def show(self, request, eventID) :
        try :
            event = Event.objects.get(event_id = eventID);
            userLogin = super(EventView, self).getUserLogin(request);
            members = EventSubscription.objects.filter(event = event);
            member = EventSubscription.objects.filter(Q(event = event) & Q(user_id = userLogin.user));

            return super(EventView, self).render(request, 'event/show.html', {
                'title' : 'event : ' + eventID,
                'event' : event,
                'members' : members,
                'member' : member,
            });
        except :
            return HttpResponseRedirect('/event/')

    #Edit event 
    def updateEvent(self, request, eventID) :
        event = Event.objects.get(event_id = eventID);
        userLogin = super(EventView, self).getUserLogin(request);

        if (event.user_id == userLogin.user.user_id) :

            return super(EventView, self).render(request, 'event/update.html', {
                'title' : eventID,
                'test' : userLogin.user.user_id,
                'event' : event,
            });
            
        return HttpResponseRedirect('/event/getEvent/' + eventID)

    #Delete event 
    def deleteEvent(self, request, eventID) :
        event = Event.objects.get(event_id = eventID);
        userLogin = super(EventView, self).getUserLogin(request);

        if (event.user_id == userLogin.user.user_id) :
            event.delete()
            return HttpResponseRedirect('/event/')

        return HttpResponseRedirect('/event/getEvent/' + eventID)

    def create(self, request) :
        userLogin = super(EventView, self).getUserLogin(request)
        new_entry = Event(title='title', user=userLogin.user, body='body', publiced='0')
        new_entry.save()

        return HttpResponseRedirect('/event/getEvent/'+ str(new_entry.event_id) +'/edit/')

    def update (self, request) :
        name = request.POST.get('name', '')
        value = request.POST.get('value', '')
        pk = request.POST.get('pk', '')

        record = Event.objects.get(event_id = pk)
        record.__setattr__(name, value)
        record.save()

        return super(EventView, self).render(request, 'event/update.html', {
            
        });

    def unsubscribe (self, request, eventID) :
        userLogin = super(EventView, self).getUserLogin(request);
        subscription = EventSubscription.objects.filter(Q(event_id = eventID) & Q(user_id = userLogin));

        subscription.delete()
        return HttpResponseRedirect('/event/getEvent/' + eventID)
    
    def subscribe (self, request, eventID) :
        userLogin = super(EventView, self).getUserLogin(request);
        eventsubscription = EventSubscription(event_id = eventID, user_id = userLogin.user.user_id)
        eventsubscription.save()

        return HttpResponseRedirect('/event/getEvent/' + eventID)
