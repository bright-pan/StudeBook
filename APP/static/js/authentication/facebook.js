/**
 * @class Facebook
 * @author StudeBook
 */
Facebook = function() {
	
	var self = this;
	
	/**
	 * @method init
	 */
	this.init = function () {
		//Init FB module
		initModule();
		//Set login button
		setButton();
	};
	
	var setButton = function() {
		//FB login button
		self.button = $('<div />');
		self.button.attr('class','button');
		self.button.attr('id', 'facebookButton');
		self.button.click(self.checkLoginState);
		self.button.append($('<a />'));
	};
	
	this.render = function(wrapper) {
		$(wrapper).append(self.button);
	};
	
	/**
	 *  This is called with the results from from FB.getLoginStatus().
	 */
	this.statusChangeCallback = function (response) {
		if (response.status === 'connected') {
	        //SB login with facebook 
	        $.post(AUTH_CONFIG.FACEBOOK.API_URI, { 
	        	'csrfmiddlewaretoken' : SB.CONFIG.CSRF_TOKEN, 
	        	'accessToken' 		  : response.authResponse.accessToken
	        }, function(response) {
	        	if(response.status == 200) {
                    localStorage.setItem('sb_user_id', response.data.sb_user_id);
                    localStorage.setItem('sb_access_token', response.data.sb_access_token);
                    return window.location.href = '/';
	        	};
			});
		} else if (response.status === 'not_authorized') {
	        // The person is logged into Facebook, but not your app.
	        console.log('Not connected');
	    };
	};
	
	/**
	 * This function is called when someone finishes with the Login
	 * Button. See the onlogin handler attached to it in the sample code below. 
	 */
	this.checkLoginState = function () {
		FB.login(self.statusChangeCallback, {
    		scope : AUTH_CONFIG.FACEBOOK.SCOPE
    	});
	};
	
	/**
	 * @method initModule
	 */
	var initModule = function() {
		window.fbAsyncInit = function() {
			//Init facebook
			FB.init({
		    	appId      : AUTH_CONFIG.FACEBOOK.APP_ID,
		    	cookie     : true,  // enable cookies to allow the server to access 
		    	xfbml      : true,  // parse social plugins on this page
		        version    : 'v2.1' // use version 2.1
		    });
		};
	};
	
};

