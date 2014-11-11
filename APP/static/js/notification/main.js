/**
 * Created by michel on 11-11-14.
 */
$().ready(function(){
    //Set chat wrapper
    $('#notification').delegate('a.notification', 'click', function() {
        var pk = $(this).attr('rel');
        var notification = $('tr.notification-'+pk);
        var disabled = notification.attr('class').indexOf('disabled') != -1 ? true : false;
        notification.addClass(disabled ? 'enabled' : 'disabled').removeClass(disabled ? 'disabled' : 'enabled');
    });
});