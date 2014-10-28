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
		button.attr('data-callback', AUTH_CONFIG.GOOGLE.CALLBACK);
		button.attr('data-approvalprompt', AUTH_CONFIG.GOOGLE.PROMPT);
		button.attr('data-clientid', AUTH_CONFIG.GOOGLE.CLIENT_ID);
		button.attr('data-requestvisibleactions', AUTH_CONFIG.GOOGLE.VISIBLE_ACTION);
		button.attr('data-cookiepolicy', AUTH_CONFIG.GOOGLE.COOKIE_POLICY);
		self.button = $('<div />');
		self.button.attr('id', 'signin-button');
		self.button.attr('class', 'show');
		self.button.append(button);
	};
};

//Google OAuth callback
var OAuthCallback = function (response) {
	//Login succes
    if (response['status']['signed_in']) {
    	//NRGWeb login with google 
        $.post(AUTH_CONFIG.GOOGLE.API_URI, { 
        	'csrfmiddlewaretoken' : SB.CONFIG.CSRF_TOKEN, 
        	'accessToken' 		  : response.access_token
        }, function(response) {
	    	alert(response.message);
	    	if(response.status == 200) {
	    		window.location.href = '/';
	    	}
		});
    //Login failure
  	} else {
	    console.log('Sign-in state: ' + response['error']);
  	};	
};
