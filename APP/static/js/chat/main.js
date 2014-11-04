var _SOCKET = null;

$().ready(function(){
	//SETUP SOCKET CONNECTION
    initSocket('ws://185.10.51.243',8020);
});

//TERMINATE SOCKET CONNECTION
window.onbeforeunload = function() {
	_SOCKET.close()
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
    userFriendList();
};

/**
 * TMP TMP TMP
 */

/**
 * @method userFriendList
 */
function userFriendList() {
    $.get(SB.CONFIG.API_URI + 'user/getFriends', function(response) {
        //Update userFriendList
        if(response.status == 200) {
            $('#userFriendList').empty();
            response.friendList.forEach(function(friend) {
                var element = $('<a />')
                element.text(friend.full_name);
                element.attr('rel', friend.pk);
                element.attr('href','#');
                element.attr('id', 'CLIENT-'+friend.pk);
                $('#userFriendList').append($('<li />').append(element));
            });
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
    switch(data.action) {
        case 'userFriendList' :
            updateFriendsList();
        default :
            console.log(data);
        break;
    };
};


