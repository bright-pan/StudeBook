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
        location.reload();
    });
}
