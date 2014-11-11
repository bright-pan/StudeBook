#SB
from APP.views.MainView import MainView
from APP.models.NotificationModel import Notification

"""
 @class NotificationView
 @version 0.1
 @author StudeBook inc.
"""

class NotificationView(MainView):

    def read (self, request) :
        userLogin = super(NotificationView, self).getUserLogin(request);
        notificationList = Notification.objects.filter(recipient = userLogin.user);
        return super(NotificationView, self).render(request, 'notification/notification.html', {
            'notification_list' : notificationList
        });