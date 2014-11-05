var _SOCKET = null;

$().ready(function(){
	//SETUP SOCKET CONNECTION
    initSocket('ws://185.10.51.243',8027);
});

window.onbeforeunload = function() {
    return disconnect();
};

/**
 * @method disconnect
 * TMP
 */
function disconnect() {
    _SOCKET.close();
    return;
    //Get friend list
    $.get(SB.CONFIG.API_URI + 'user/getFriends', function(response) {
        if(response.status == 200) {
            var pks = [];
            response.friendList.forEach(function(friend) { pks.push(friend.pk); });
            //Validate user friend status
            _SOCKET.send(JSON.stringify({ action : 'notifyClient', clientList : pks, 'message' : 'disconnected' }));
            _SOCKET.close();
        }
    });
};

/**
 * @method connect
 * TMP
 */
function connect() {
    //Get friend list
    $.get(SB.CONFIG.API_URI + 'user/getFriends', function(response) {
        if(response.status == 200) {
            var pks = [];
            response.friendList.forEach(function(friend) { pks.push(friend.pk); });
            //Validate user friend status
            _SOCKET.send(JSON.stringify({ action : 'notifyClient', clientList : pks, 'message' : 'connected' }));
        }
    });
};

/**
 * @method initSocket
 * @param <String> host
 * @param <Integer> port
 */
function initSocket(host, port, userID) {
	//Init socket
	_SOCKET = new WebSocket(host + ':' + port);
	//Send opening message
	_SOCKET.onopen = onOpen;
	//Incoming message
	_SOCKET.onmessage = onMessage;
    //update friends list
    updateUserFriendList();
};

/**
 * @method updateUserFriendStatus
 */
function updateUserFriendStatus(friendStatus) {
    friendStatus.forEach(function(friend){
        var element = $('#'+friend.clientID);
        if(friend.status == 'connected') {
            element.addClass('online').removeClass('offline');
        } else {
            element.removeClass('online').addClass('offline');
        };
    });
};

/**
 * @method validateUserFriendStatus
 */
function validateUserFriendStatus() {
    //Validate user friend status
    _SOCKET.send(JSON.stringify({ action : 'validateClient', clientList : pks }));
};

/**
 * @method updateUserFriendList
 */
function updateUserFriendList() {
    $.get(SB.CONFIG.API_URI + 'user/getFriends', function(response) {
        //Update userFriendList
        if(response.status == 200) {
            var pks = [];
            $('#userFriendList').empty();
            response.friendList.forEach(function(friend) {
                pks.push(friend.pk);
                var element = $('<li />').attr('id','CLIENT-'+friend.pk);
                var inner = $('<a />');
                inner.text(friend.full_name);
                inner.attr('rel', friend.pk);
                inner.attr('href','#');
                element.append(inner);
                $('#userFriendList').append(element);
            });
            //Validate user friend status
            validateUserFriendStatus();
        }
    });
};

/**
 * @method onOpen
 */
var onOpen = function () {
    //Get user info
    $.get(SB.CONFIG.API_URI + 'user/getInfo', function(response) {
        //Setup socket connection with server
        if(response.status == 200) {
            _SOCKET.send(JSON.stringify({ action : 'initClient', clientID : response.user.pk }));
        };
    });
};

/**
 * @method onMessage
 */
var onMessage = function(response) {
    var data = JSON.parse(response.data);
    console.log(data);
    switch(data.action) {
        case 'init' :
            _SOCKET.send(JSON.stringify({ action : 'notifyClient', clientList : pks, message : 'connected' }));
        break;
        case 'clientStatus' :
            updateUserFriendStatus(data.clientList);
        break;
        //TMP!!!
        case 'ping' :
            validateUserFriendStatus();
        default :
            console.log(data);
        break;
    };
};


