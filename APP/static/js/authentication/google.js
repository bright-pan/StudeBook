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
		gapi.signin.render(self.button.attr('id'), {
	      'callback'			  : self.OAuthCallback,
	      'clientid'			  : AUTH_CONFIG.GOOGLE.CLIENT_ID,
	      'cookiepolicy'		  : AUTH_CONFIG.GOOGLE.COOKIE_POLICY,
	      'requestvisibleactions' : AUTH_CONFIG.GOOGLE.VISIBLE_ACTION,
	      'scope'		          : AUTH_CONFIG.GOOGLE.SCOPE,
	      'approvalprompt' 		  : AUTH_CONFIG.GOOGLE.PROMPT
	    });
	};
	
	//Google OAuth callback
	this.OAuthCallback = function (response) {
		//Login succes
		if (response['status']['signed_in']) {
			console.log(response);
	    	//NRGWeb login with google 
	        $.post(AUTH_CONFIG.GOOGLE.API_URI, { 
	        	'csrfmiddlewaretoken' : SB.CONFIG.CSRF_TOKEN, 
	        	'accessToken' 		  : response.access_token
	        }, function(response) {
	        	if(response.status == 200) {
		    		return window.location.href = '/';
		    	}
                alert(response.message);
			});
	    //Login failure
	  	} else {
		    console.log('Sign-in state: ' + response['error']);
	  	};	
	};
	
	/**
	 * @method setButton
	 */
	var setButton = function() {
		//Google login button
		self.button = $('<div />');
		self.button.attr('class','button');
		self.button.attr('id', 'googleButton');
		self.button.append($('<a />'));
	};
};
