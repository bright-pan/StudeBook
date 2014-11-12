/********************************************
*** COPYRIGHT : J. Plat, STUDEBOOK  2014 ***
********************************************/

/**
 * @class StudeBookUpdates
 */
var StudeBookUpdates = function() {

    var self = this;

    /**
     * @method init
     * Initialize StudeBookUpdates
     */
    this.init = function() {
        
        self.update();
        setInterval(function () {self.update()}, 5000);

    };

    /**
     * @method update
     * (Re)render update list
     */
    this.update = function() {
        var URI = SB.CONFIG.API_URI + 'update/getUpdates';

        $.get(URI, function(response) {

            if(response.status == 200) {
                var list = '<ul class="nav navbar-stacked">';
                response.data.updateList.forEach(function(update) {
                    list = list + '<li style="border-bottom: 1px solid black;"><a href="' + update.link + '" style="color: black; font-size: 12x;">' + update.content + '</a></li>';
                });
                list = list + '</ul>';
                $('#updateList').html(list);
            }
        });
    };

};


/**
 * Load when DOM is ready
 */
$().ready(function(){
    var updates = new StudeBookUpdates();
    updates.init();
});


