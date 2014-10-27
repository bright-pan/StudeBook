$(document).ready(function() {
    console.log('Document ready');
    initEditable();
});

function initEditable() {
    $.fn.editable.defaults.mode = 'inline-block';
    $.fn.editable.defaults.ajaxOptions = {
        type: "post"
    };

    var options = {
        success: function(response) {
            if (!response.success) {
                return response.message;
            }
        },
        params: function(params) {
            var data = {};

            if (params.name === '' && typeof params.value === 'object') {
                data = params.value;
            } else {
                data[params.name] = params.value;
            }
            return data;
        }
    };

    $('.editable').each(function() {
        $(this).editable(options);
    });
    $('.date').each(function() {
        $(this).editable({
            type: 'date',
            format: 'yyyy-mm-dd',
            viewformat: 'yyyy-mm-dd',
            datepicker: {
                weekStart: 1
            },
            forceParse: true
        });
    });
}
