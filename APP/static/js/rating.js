$(document).ready(function() {
    
    $('.starRating').click(function() {
        var rating = $(this).attr('id').replace('starRating', ''),
            fileId = $('#fileId').val();

        $.post(SB.CONFIG.BASE_URI + "file/addRating/", {fileId: fileId, rating: rating, csrfmiddlewaretoken: SB.CONFIG.CSRF_TOKEN}, function(result) {
            console.log(result);
            if (result.status == '200') {
                
                for ( i = 1; i <= 5; i ++ ) {
                    if (i != result.avgRating) {
                        $('#starRating' + i).html('<span>Give it ' + i + ' star(s)</span>');
                    } else {
                        $('#starRating' + i).html('<span>Give it ' + i + ' star(s)</span><b></b>');
                    }
                }

                $('#averageRating').html(result.avgRating);
                $('#numberOfRatings').html(result.numberOfRatings)

            }
        });
    });

});