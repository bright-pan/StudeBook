$(document).ready(function() {
    bindButtons()
});

function bindButtons() {

    $('.de-friend').on('click', function() {
        var user = $(this).parent().data('user-id');
        $.ajax({
            method: 'GET',
            url: "remove/" + user
        });
        $(this).prop('disabled', true);
        $(this).html('Removed');

    });
    $('.block').on('click', function() {
        var user = $(this).parent().data('user-id');
        var currentUser = $(this).parent().data('current-user');
        if (user == currentUser) {
            alert('Ya can\'t block yourself stoopid. And you\'re stupid for even trying this.');
        } else {
            $.ajax({
                method: 'GET',
                url: "block/" + user
            });
            $(this).prop('disabled', true);
            $(this).html('Blocked');
        }
    });
}
