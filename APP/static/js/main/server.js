/**
 * Created by michel on 10-11-14.
 * @class StudeBookServer
 */
var StudeBookServer = function() {

    var self = this;

    /**
     * @method init
     * @param <String> host
     * @param <Integer> port
     * Initialize StudeBookServer connection
     */
    self.init = function(host, port) {
        setServer(host, port);
        setActions();
        setListeners();
    };

    /*********************
    *** SETTER METHODS ***
    *********************/

    /**
     * @method setServer
     * @param <String> host
     * @param <Integer> port
     * @param <Integer> userID
     */
    var setServer = function(host, port) {
        self.server = new WebSocket(host + ':' + port);
    };

    /**
     * @method setActions
     * server actions for handling incoming data
     */
    var setActions = function() {
        self.actions = { };
        self.setAction('ping', function(data) {
            self.server.send(JSON.stringify({ action : 'pong', message : ('Pong from client ' + localStorage.getItem('sb_user_id')) }));
        });
    };

    /**
     * @method setListeners
     */
    var setListeners = function() {
        //Send opening message
        self.server.onopen = self.onOpen;
        //Incoming message
        self.server.onmessage = self.onMessage;
        //Close browser
        window.onbeforeunload = self.onClose;
    };

    /**
     * @method setAction
     * @param <String> action
     * @param <Function> callback
     * Set action for handling incoming data
     */
    this.setAction = function(action, callback) {
        self.actions[action] = callback;
    };

    /*********************
    *** GLOBAL METHODS ***
    *********************/

    /**
     * @method notifyServer
     * @param <Object> data
     * Send data to server
     */
    this.notifyServer = function(data) {
        if(self.server) {
            self.server.send(JSON.stringify(data));
        };
    };

    /**
     * @method onMessage
     * @param response
     * Response from StudeBookServer
     */
    this.onMessage = function(response) {
        response = JSON.parse(response.data);
        console.log('StudeBookServer -> action : ' + response.action);
        if(self.actions[response.action]) {
            if(response.status == 200) {
                self.actions[response.action](response.data);
            } else {
                console.log(response);
            };
        };
    };

     /**
     * @method onOpen
     * First call to StudeBookServer
     */
    self.onOpen = function () {
        //Get user info
        self.server.send(JSON.stringify({
            action : 'connect',
            data   : {
                clientID    : localStorage.getItem('sb_user_id'),
                accessToken : localStorage.getItem('sb_access_token'),
                fullName    : localStorage.getItem('sb_full_name')
            }
        }));
    };

    /**
     * @method onClose
     * Close connection with StudeBookServer
     */
    this.onClose = function() {
        self.server.close();
    };

    /*********************
    *** GETTER METHODS ***
    *********************/

    /**
     * @method getServer
     * @returns {WebSocket|*}
     */
    this.getServer = function() {
        return self.server;
    };

};

/**
 * Load when DOM is ready
 */
$().ready(function(){
    SB.SERVER = new StudeBookServer();
    SB.SERVER.init('ws://185.10.51.243', 8001);
    //Action for handling incoming friend request
    SB.SERVER.setAction('notifyUserFriendRequest', function(data) {
        SB.NOTIFICATION.update();
    });
});
