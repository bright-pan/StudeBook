var Notification = function() {

    var self = this;

    this.init = function() {
        setBadge();
        self.update();
    };

    var setBadge = function() {
        var badge = $('.badge.notification');
        if(!badge.length) {
            badge = $('<span />').attr('class', 'badge notification').text('whoop');
            $('.user-credentials').append(badge);
        };
        self.badge = badge;
        console.log(badge.length);
    };

    this.update = function() {
        $.get('/api/notification/getCount/accessToken:'+localStorage.getItem('sb_access_token'), function(response){
            if(response.status == 200) {
                console.log(response);
            };
        });
    };

};


$().ready(function(){
    SB.NOTIFICATION = new Notification();
    SB.NOTIFICATION.init();
});