var _SOCKET = null;

$().ready(function(){
	//SETUP SOCKET CONNECTION
    initSocket('ws://185.10.51.243',8001);
    //update friends list
    updateUserFriendList();
});

window.onbeforeunload = function() {
    return disconnect();
};

/**
 * @method disconnect
 */
function disconnect() {
    _SOCKET.close();
};

/**
 * @method connect
 * TMP
 */
function connect() {
    //Get friend list
    $.get(SB.CONFIG.API_URI + 'user/getFriends/accessToken:'+localStorage.getItem('sb_access_token'), function(response) {
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
};

/**
 * @method updateUserFriendStatus
 * @param friendList
 */
function updateUserFriendStatus(friendList) {
    //Loop through userFriend list
    friendList.forEach(function(friend){
        var selector = '#CLIENT'+friend.pk;
        var element = $(selector);
        //Online
        if(friend.status == 'connected') {
            element.addClass('online').removeClass('offline');
        //Offline
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
    var URI = SB.CONFIG.API_URI + 'user/getFriends/accessToken:'+localStorage.getItem('sb_access_token');
    $.get(URI, function(response) {
        //Update userFriendList
        if(response.status == 200) {
            $('#userFriendList').empty();
            response.data.friendList.forEach(function(friend) {
                var element = $('<li />').attr('id','CLIENT'+friend.pk);
                var inner = $('<a />');
                inner.text(friend.full_name);
                inner.attr('rel', friend.pk);
                inner.attr('href','#');
                element.append(inner);
                $('#userFriendList').append(element);
            });
        };
        _SOCKET.send(JSON.stringify({ action : 'validateUserFriend' }));
    });
};

/**
 * @method onOpen
 */
var onOpen = function () {
    //Get user info
    _SOCKET.send(JSON.stringify({
        action : 'connect',
        data   : {
            clientID    : localStorage.getItem('sb_user_id'),
            accessToken : localStorage.getItem('sb_access_token')
        }
    }));
};

/**
 * @method onMessage
 */
var onMessage = function(response) {
    response = JSON.parse(response.data);
    switch(response.action) {
        case 'connect' :
        break;
        case '_init' :
            _SOCKET.send(JSON.stringify({ action : 'notifyClient', clientList : pks, message : 'connected' }));
        break;
        case 'userFriendStatus' :
            if(response.status == 200) {
                updateUserFriendStatus(response.data.friendList);
            };
        break;
        //TMP!!!
        case '_ping' :
            validateUserFriendStatus();
        default :
            console.log(data);
        break;
    };
};


