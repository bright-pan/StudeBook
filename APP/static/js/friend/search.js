$(document).ready(function() {
    bindButtons()
});

function bindButtons() {
    $('.cancel-request').mouseenter(function() {
        $(this).html('Cancel request');
    });
    
    $('.cancel-request').mouseleave(function() {
        $(this).html('Pending...');
    });

    $('.de-friend').on('click', function() {
        var user = $(this).parent().data('user-id');
        $.ajax({
            method: 'GET',
            url: "../remove/" + user
        });
        $(this).prop('disabled', true);
        $(this).html('Removed');

    });

    $('.add-friend').on('click', function() {
        var user = $(this).parent().data('user-id');
        var currentUser = $(this).parent().data('current-user');
        if (user == currentUser) {
            alert('Ya can\'t add yourself stoopid. You must really love yourself. And you\'re stupid for even trying this.');
        } else {
            $.ajax({
                method: 'GET',
                url: "../add/" + user
            });
            $(this).prop('disabled', true);
            $(this).html('Request sent');

            /********************
             *** NOTIFICATION ***
             *******************/
            var URI = '/api/notification/create/accessToken:'+localStorage.getItem('sb_access_token') + '/';
            $.post(URI, {
                notification        : 'Would you be my friend?',
	        	csrfmiddlewaretoken : SB.CONFIG.CSRF_TOKEN,
                category            : 'Friend request',
                recipient_id        : user
            }, function(response) {
                console.log(response);
                if(response.status == 200) {
                    SB.SERVER.notifyServer({
                        action : 'notifyUserFriendRequest',
                        data   : {
                            clientID : user
                        }
                    });
                };
            });
        };
    });

    $('.accept-friend').on('click', function() {
        var user = $(this).parent().data('user-id');
        var currentUser = $(this).parent().data('current-user');
        if (user == currentUser) {
            alert('Ya can\'t add yourself stoopid. You must really love yourself. And you\'re stupid for even trying this.');
        } else {
            $.ajax({
                method: 'GET',
                url: "../add/" + user
            });
            $(this).prop('disabled', true);
            $(this).html('Accepted');
        }
    });

    $('.block').on('click', function() {
        var user = $(this).parent().data('user-id');
        var currentUser = $(this).parent().data('current-user');
        if (user == currentUser) {
            alert('Ya can\'t block yourself stoopid. And you\'re stupid for even trying this.');
        } else {
            $.ajax({
                method: 'GET',
                url: "../block/" + user
            });
            $(this).prop('disabled', true);
            $(this).html('Blocked');
        }
    });

    $('.cancel-request').on('click', function() {
        var user = $(this).parent().data('user-id');
        var currentUser = $(this).parent().data('current-user');
        $.ajax({
            method: 'GET',
            url: "../cancel/" + user
        });
        $(this).prop('disabled', true);
        $(this).html('Canceled');
    });

    $('.un-block').on('click', function() {
        var user = $(this).parent().data('user-id');
        $.ajax({
            method: 'GET',
            url: "../undoBlock/" + user
        });
        $(this).prop('disabled', true);
        $(this).html('Unblocked');
    });


}
