var _SOCKET = null;

/**
 * Load when DOM is ready
 */
$().ready(function(){
	//SETUP SOCKET CONNECTION
    initSocket('ws://185.10.51.243',8001);
    //update friends list
    updateUserFriendList();

    //TMP
    $('#userFriendList').delegate('a.userFriend.online', 'click', function() {
        var box = getChatBox($(this).text());
        box.draggable({ containment : 'body' });
        $('.main').append(box);
    });

});

/**
 * Call when browser window is closing
 * @returns {*}
 */
window.onbeforeunload = function() {
    return disconnect();
};

/**
 * @method disconnect
 * Close connection with StudeBookServer
 */
function disconnect() {
    _SOCKET.close();
};

/**
 * @method initSocket
 * @param <String> host
 * @param <Integer> port
 * Initialize StudeBookServer socket connection
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
 * @method updateUserFriendList
 * (Re)render userFriend list
 */
function updateUserFriendList() {
    var URI = SB.CONFIG.API_URI + 'user/getFriends/accessToken:'+localStorage.getItem('sb_access_token');
    $.get(URI, function(response) {
        //Update userFriendList
        if(response.status == 200) {
            $('#userFriendList').empty();
            response.data.friendList.forEach(function(friend) {
                var element = $('<a />');
                element.text(friend.full_name);
                element.attr('class','userFriend');
                element.attr('rel', friend.pk);
                element.attr('href','#');
                $('#userFriendList').append($('<li />').append(element));
            });
        };
        //Validate user friend status
        validateUserFriendStatus();
    });
};

/**
 * @method updateUserFriendStatus
 * @param friendList
 */
function updateUserFriendStatus(friendList) {
    //Loop through userFriend list
    friendList.forEach(function(friend){
        //Element
        var element = $('a.userFriend[rel='+friend.pk+']');
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
    if(_SOCKET) {
        _SOCKET.send(JSON.stringify({ action : 'validateUserFriend' }));
    };
};

/**
 * @method onOpen
 * First call to StudeBookServer
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
 * @param response
 * Response from StudeBookServer
 */
var onMessage = function(response) {
    response = JSON.parse(response.data);
    switch(response.action) {
        case 'connect' :
            //TODO fill
        break;
        case 'userFriendStatus' :
            if(response.status == 200) {
                updateUserFriendStatus(response.data.friendList);
            };
        break;
        case '_ping' :
            //TMP!!!
            validateUserFriendStatus();
        break;
        default :
            console.log(response);
        break;
    };
};

/**
 * @method getChatBox
 * @param title
 * @returns {*|jQuery|HTMLElement}
 */
var getChatBox = function(title) {
    var wrapper = $('<div />').attr('class', 'popover top');
    var arrow = $('<div />').attr('class','arrow');
    var header = $('<h3 />').attr('class', 'popover-title');
    var title = $('<a />').text(title).attr('class','title');
    var content = $('<div />').attr('class', 'popover-content');
    var close = $('<a />').attr('class', 'btn btn-warning').text('X').click(function(){
        wrapper.remove();
    });
    header.append(title).append(close);
    wrapper.append(arrow).append(header).append(content);
    return wrapper;
};


