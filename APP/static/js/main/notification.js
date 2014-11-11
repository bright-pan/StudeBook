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
        var badge = $('.badge.notification');
        if(!badge.length) {
            badge = $('<span />').attr('class', 'badge notification');
            $('.user-credentials').append(badge);
        };
        return badge;
    };

    /**
     * @method update
     * Check weather there are notifications or not
     */
    this.update = function() {
        $.get('/api/notification/getCount/accessToken:'+localStorage.getItem('sb_access_token'), function(response){
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
            self.badge = self.setBadge();
        };
        //Update badge
        if(number) {
            return self.badge.text(number);
        };
        //Remove badge
        if(self.badge) {
            self.badge.remove();
        };
    };
};

$().ready(function(){
    SB.NOTIFICATION = new Notification();
    SB.NOTIFICATION.init();
});