/**
 * Created by michel on 11-11-14.
 */
$().ready(function(){
    //Set chat wrapper
    $('#notification').delegate('a.notification', 'click', function() {
        //Toggle notification body
        var pk = $(this).attr('rel');
        var notification = $('tr.notification-'+pk);
        var disabled = notification.attr('class').indexOf('disabled') != -1 ? true : false;
        notification.addClass(disabled ? 'enabled' : 'disabled').removeClass(disabled ? 'disabled' : 'enabled');
        //Unread message
        if($(this).attr('class').indexOf('unread') != -1) {
            //Update status
            var parent = $(this).closest('tr');
            parent.find('.status').text('read');
            $(this).addClass('read').removeClass('unread');
            SB.NOTIFICATION.updateStatus(pk);
        };
    });
});