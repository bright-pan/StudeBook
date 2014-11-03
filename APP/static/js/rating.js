$(document).ready(function() {
    
    $('.starRating').click(function() {
        var rating = $(this).attr('id').replace('starRating', ''),
            fileId = $('#fileId').val();

        $.post(SB.CONFIG.BASE_URI + "file/addRating/", {fileId: fileId, rating: rating, csrfmiddlewaretoken: SB.CONFIG.CSRF_TOKEN}, function(result) {
            console.log(result);
        });
    });

});