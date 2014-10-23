//GOOGLE Config Setting
var GOOGLE_CONFIG = {
	OAUTH_CALLBACK : 'OAuthCallback',
	OAUTH_PROMPT   : 'force',
	CLIENT_ID      : '992449209428-btink9cn4rkd9ka3e1uqo3v5kg7fvcf3.apps.googleusercontent.com',
	VISIBLE_ACTION : 'http://schema.org/CommentAction',
	COOKIE_POLICY  : 'single_host_origin'
};

//Google OAuth callback
var OAuthCallback = function (response) {
	
	console.log(response);
	return;
	
	//Login succes
    if (response['status']['signed_in']) {
    	//DJANGO CSRF TOKEN
		var csrf = $('input[name="csrfmiddlewaretoken"]').val();
		var base = CONFIG.API_URI + 'externalAccountLogin';
		//NRGWeb login with google 
        $.post(base, { 
        	'csrfmiddlewaretoken' : csrf, 
        	'userID'              : authResult.client_id, 
        	'accessToken' 		  : authResult.access_token,
        	'type'        		  : 'google'
        }, function(resp) {
	    	alert('Google : ' + resp.message);
	    	if(resp.status == 200) {
	    		window.location.href = '/';
	    	};
		});
    //Login failure
  	} else {
	    console.log('Sign-in state: ' + authResult['error']);
  	};	
};

/**
 * @class Google
 * @author StudeBook
 */
var Google = function() {
	
	var self = this;
	
	/**
	 * @method init
	 */
	this.init = function() {
		setButton();
	};
	
	/**
	 * @method render
	 * @param <String> wrapper
	 */
	this.render = function(wrapper) {
		$(wrapper).append(self.button);
	};
	
	/**
	 * @method setButton
	 */
	var setButton = function() {
		var button = $('<div />');
		button.attr('class', 'g-signin');
		button.attr('data-callback', GOOGLE_CONFIG.OAUTH_CALLBACK);
		button.attr('data-approvalprompt', GOOGLE_CONFIG.OAUTH_PROMPT);
		button.attr('data-clientid', GOOGLE_CONFIG.CLIENT_ID);
		button.attr('data-requestvisibleactions', GOOGLE_CONFIG.VISIBLE_ACTION);
		button.attr('data-cookiepolicy', GOOGLE_CONFIG.COOKIE_POLICY);
		self.button = $('<div />');
		self.button.attr('id', 'signin-button');
		self.button.attr('class', 'show');
		self.button.append(button);
	};
	
};
