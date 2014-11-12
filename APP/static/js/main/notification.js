var Notification = function() {

    var self = this;

    this.init = function() {
        self.update();
    };

    /**
     * @method setBadge
     * @returns {*|jQuery|HTMLElement}
     * Create and render badge element
     */
    this.setBadge = function() {
        self.badge = $('.badge.notification');
        if(!self.badge.length) {
            self.badge = $('<span />').attr('class', 'badge notification');
            self.clone = self.badge.clone();
            $('.profile .user-credentials').append(self.badge);
            $('.profile .notifications').append(self.clone);
        };
    };

    /**
     * @method update
     * Check weather there are notifications or not
     */
    this.update = function() {
        console.log('Notification -> update');
        var URI = '/api/notification/getCount/accessToken:'+localStorage.getItem('sb_access_token') + '/';
        $.get(URI, function(response){
            if(response.status == 200) {
                self.updateBadge(parseInt(response.data.unread));
            };
        });
    };

    /**
     * @method updateStatus
     * @param notificationID
     */
    this.updateStatus = function(notificationID, read) {
        var URI = '/api/notification/update/accessToken:'+localStorage.getItem('sb_access_token') + '/';
        $.post(URI, {
            notification_id     : notificationID,
            read                : read || 1,
            csrfmiddlewaretoken : SB.CONFIG.CSRF_TOKEN
        }, function(response) {
            console.log(response);
            if(response.status == 200) {
                self.updateBadge(parseInt(response.data.unread));
            };
        });
    };

    /**
     * @method updateBadge
     * @param number
     * @returns {*}
     * Update badge text
     */
    this.updateBadge = function(number) {
        if(!self.badge && number) {
            self.setBadge();
        };
        //Update badge
        if(number) {
            self.badge.text(number);
            self.clone.text(number);
        } else if (self.badge) {
            self.badge.remove();
            self.clone.remove();
        };
    };
};

$().ready(function(){
    SB.NOTIFICATION = new Notification();
    SB.NOTIFICATION.init();
    setInterval(SB.NOTIFICATION.update,10000);
});