//AUTHENTICATION CONFIG
var AUTH_CONFIG = {
	//GOOGLE AUTH
	GOOGLE : {
		PROMPT   	   : 'force',
		CLIENT_ID      : '992449209428-btink9cn4rkd9ka3e1uqo3v5kg7fvcf3.apps.googleusercontent.com',
		VISIBLE_ACTION : 'http://schema.org/CommentAction',
		COOKIE_POLICY  : 'single_host_origin',
		API_URI        : SB.CONFIG.API_URI + 'externalAccountLogin/provider:google/',
		SCOPE		   : new Array(
			'https://www.googleapis.com/auth/plus.login',
			'https://www.googleapis.com/auth/userinfo.email',
			'https://www.googleapis.com/auth/userinfo.profile'
		).join(' ')
	},
	//FACEBOOK AUTH
	FACEBOOK : {
		APP_ID  : 307740626096646,
		SDK_URI : '//connect.facebook.net/nl_NL/sdk.js',
		API_URI : SB.CONFIG.API_URI + 'externalAccountLogin/provider:facebook/',
		SCOPE   : 'public_profile,email'
	},
	//LOGOUT 
	LOGOUT : {
		API_URI : SB.CONFIG.API_URI + 'externalAccountLogin/logout/'
	}
};

//Execute after the DOM is ready.
$().ready(function() {
    //Logout button
	$('#logout').click(function() {
		$.post(AUTH_CONFIG.LOGOUT.API_URI, { 
        	'csrfmiddlewaretoken' : SB.CONFIG.CSRF_TOKEN
        }, function(response) {
	    	if(response.status == 200) {
	    		window.location.href = '/';
	    	};
		});
	});
	//FACEBOOK OAUTH
	var facebook = new Facebook();
	facebook.init();
	facebook.render('#OAuth');
	//GOOGLE OAUTH
	var google = new Google();
	google.init();
	google.render('#OAuth');
});