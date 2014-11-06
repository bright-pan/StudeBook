/********************************************
****** COPYRIGHT : M.JANSMA  2014 ***********
********************************************/

var _SOCKET = null;

/**
 * Load when DOM is ready
 */
$().ready(function(){
	//SETUP SOCKET CONNECTION
    initSocket('ws://185.10.51.243',8001);
    //update friends list
    updateUserFriendList();
    //Set chat wrapper
    $('#userFriendList').delegate('a.userFriend.online', 'click', function() {
        var box = getChatWrapper($(this).text(), $(this).attr('rel'));
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
 * @method handleNotifyUserFriend
 * @param data
 * Handle incoming notification
 */
function handleNotifyUserFriend(data) {
    var box = $('#CLIENT'+data.pk);
    console.log(box);
    if(!box.length) {
        //Render chat wrapper
        box = getChatWrapper(data.fullName,data.pk);
        box.draggable({ containment : 'body' });
        $('.main').append(box);
    };
    //Add message to chatContainer
    box.find('.chatContainer').prepend($('<p />').text(data.message));
};

/**
 * @method notifyUserFriend
 * @param userID
 * @param message
 * Notify userFriend by userID
 */
function notifyUserFriend(userID, message) {
    //Notify user friend
    if(_SOCKET) {
        _SOCKET.send(JSON.stringify({
            action : 'notifyUserFriend',
            data   : {
                clientID : userID,
                message  : message
            }
        }));
    };
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
            accessToken : localStorage.getItem('sb_access_token'),
            fullName    : localStorage.getItem('sb_full_name')
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
        case 'notifyUserFriend' :
            if(response.status == 200) {
                handleNotifyUserFriend(response.data);
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
 * @method getChatWrapper
 * @param username
 * @param userID
 * @returns {*|jQuery|HTMLElement}
 */
var getChatWrapper = function(username, userID) {
    var wrapper = $('<div />').attr('class', 'popover top chatWrapper').attr('id','CLIENT'+userID);
    var arrow = $('<div />').attr('class','arrow');
    var header = $('<h3 />').attr('class', 'popover-title header');
    var title = $('<a />').text(username).attr('class','title');
    var content = $('<div />').attr('class', 'popover-content content');
    var chatContainer = $('<div />').attr('class', 'chatContainer');
    var chatBox = $('<input />').attr('type','text').attr('class','chatBox').attr('placeholder','Say hi...');
    var close = $('<a />').attr('class', 'btn btn-warning').text('X');
    chatBox.keyup(function(e){
        var message = $(this).val();
        if(e.keyCode == 13 && message) {
            chatContainer.prepend($('<p />').attr('class','me').text(message));
            notifyUserFriend(userID, message);
            $(this).val('');
        };
    });
    close.click(function(){ wrapper.remove(); });
    content.append(chatContainer).append(chatBox);
    header.append(title).append(close);
    wrapper.append(arrow).append(header).append(content);
    return wrapper;
};


