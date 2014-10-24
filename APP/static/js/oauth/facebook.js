//FB CONFIG SETTINGS
var FB_CONFIG = {
	APP_ID  : 307740626096646,
	SDK_URI : '//connect.facebook.net/nl_NL/sdk.js',
	API_URI : SB.CONFIG.API_URI + 'externalAccountLogin/provider:facebook'
};

//alert(SB.CONFIG.CSRF_TOKEN);

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
		//Load FB module
		loadModule();
		//Init FB module
		initModule();
		//Set login button
		setButton();
	};
	
	var setButton = function() {
		self.button = $('<fb:login-button />');
		self.button.attr('scope', 'public_profile,email');
		self.button.attr('onlogin', 'facebook.checkLoginState();');
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
	        $.post(FB_CONFIG.API_URI, { 
	        	'csrfmiddlewaretoken' : SB.CONFIG.CSRF_TOKEN, 
	        	'accessToken' 		  : response.authResponse.accessToken
	        }, function(response) {
	        	console.log(response);
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
		FB.getLoginStatus(self.statusChangeCallback);
	};
	
	/**
	 * @method initModule
	 */
	var initModule = function() {
		window.fbAsyncInit = function() {
			//Init facebook
			FB.init({
		    	appId      : FB_CONFIG.APP_ID,
		    	cookie     : true,  // enable cookies to allow the server to access 
		    	xfbml      : true,  // parse social plugins on this page
		        version    : 'v2.1' // use version 2.1
		    });
		};
	};
	
	/**
	 * @method loadModule
	 */
	var loadModule = function() {
		//Execute
		(function(d, s, id) {
		    var js, fjs = d.getElementsByTagName(s)[0];
		    if (d.getElementById(id)) return;
	    	js = d.createElement(s); js.id = id;
	    	js.src = FB_CONFIG.SDK_URI;
	    	fjs.parentNode.insertBefore(js, fjs);
		}(document, 'script', 'facebook-jssdk'));
	};
	
};

