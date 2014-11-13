var SB = { };
SB.CONFIG = {};
SB.CONFIG.CSRF_TOKEN = $.cookie('csrftoken');
SB.CONFIG.BASE_URI = 'http://185.10.51.243:8000/';
SB.CONFIG.API_URI = SB.CONFIG.BASE_URI + 'api/';

$().ready(function() {
});
