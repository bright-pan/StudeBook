$(document).ready(function() {
    bindButtons()
});

function bindButtons() {
    $('.send-message').on('click', function() {
        var user = $(this).parent().data('target-user');
        var currentUser = $(this).parent().data('current-user');
        var message = $(this).parent().find('textarea').val();
        $.ajax({
            method: 'POST',
            url: "/profile/send_message/",
            data: {
                current_user: currentUser,
                target_user: user,
                message: message,
                csrfmiddlewaretoken: SB.CONFIG.CSRF_TOKEN
            }
        });
        $(this).parent().find('textarea').val('');

        /********************
         *** NOTIFICATION ***
         *******************/
        // var URI = '/api/notification/create/accessToken:' + localStorage.getItem('sb_access_token') + '/';
        // $.post(URI, {
        //     notification: 'Would you be my friend?',
        //     goto_url: '/friends/request/',
        //     csrfmiddlewaretoken: SB.CONFIG.CSRF_TOKEN,
        //     category: 'Friend request',
        //     recipient_id: user
        // }, function(response) {
        //     console.log(response);
        //     if (response.status == 200) {
        //         SB.SERVER.notifyServer({
        //             action: 'notifyUserFriendRequest',
        //             data: {
        //                 clientID: user
        //             }
        //         });
        //     };
        // });
    });
}
