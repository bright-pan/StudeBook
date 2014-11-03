$(document).ready(function() {
    bindButtons()
});

function bindButtons() {
    $('.add-friend').on('click', function() {
        var user = $(this).parent().data('user-id');
        var currentUser = $(this).parent().data('current-user');
        if (user == currentUser) {
            alert('Ya can\'t add yourself stoopid. You must really love yourself. And you\'re stupid for even trying this.');
        } else {
            $(this).prop('disabled', true);
            $(this).html('Request sent');
        }

    });
    $('.block').on('click', function() {
        var user = $(this).parent().data('user-id');
        var currentUser = $(this).parent().data('current-user');
        if (user == currentUser) {
            alert('Ya can\'t block yourself stoopid. And you\'re stupid for even trying this.');
        } else {
            $(this).prop('disabled', true);
            $(this).html('Blocked');
        }

    });
}
