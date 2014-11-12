/********************************************
*** COPYRIGHT : M.JANSMA, STUDEBOOK  2014 ***
********************************************/

/**
 * @class StudeBookChat
 */
var StudeBookChat = function() {

    var self = this;

    /**
     * @method init
     * Initialize StudeBookChat
     */
    this.init = function() {
        //update friends list
        self.updateUserFriendList();
        //Set actions for handling incoming data
        setActions();
        //Set chat wrapper
        $('#userFriendList').delegate('a.userFriend.online', 'click', function() {
            var wrapper = self.getChatWrapper($(this).attr('rel'));
            if(!wrapper) {
                self.renderChatWrapper(self.setChatWrapper($(this).text(), $(this).attr('rel')));
            };
        });
    };

    /*********************
    *** GLOBAL METHODS ***
    *********************/

    /**
     * @method notifyUserFriend
     * @param userID
     * @param message
     * Notify userFriend by userID
     */
    this.notifyUserFriend = function(userID, message) {
        //Notify user friend
        SB.SERVER.notifyServer({
            action : 'notifyUserFriend',
            data   : {
                clientID : userID,
                message  : message
            }
        });
    };

    /**
     * @method validateUserFriendStatus
     */
    this.validateUserFriendStatus = function() {
        //Validate user friend status
        SB.SERVER.notifyServer({ action : 'validateUserFriend' });
    };

    /*********************
    *** GETTER METHODS ***
    *********************/

    /**
     * @method getChatWrapper
     * @param userID
     * @returns {*|jQuery|HTMLElement}
     */
    this.getChatWrapper = function(userID) {
        var wrapper = $('#CLIENT'+userID);
        if(wrapper.length) {
            return wrapper;
        };
        return false;
    };

    /*********************
    *** SETTER METHODS ***
    *********************/

    /**
     * @method setAction
     * Set actions for handling incoming data
     */
    var setActions = function() {
        //Update user friend status action
        SB.SERVER.setAction('userFriendStatus', function(data){
            self.updateUserFriendStatus(data.friendList);
        });
        //Notify user friend action
        SB.SERVER.setAction('notifyUserFriend', function(data) {
            self.handleNotifyUserFriend(data);
        });
    };

    /**
     * @method setChatWrapper
     * @param username
     * @param userID
     */
    this.setChatWrapper = function(username, userID) {
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
                chatContainer.append($('<p />').attr('class','me').text(message));
                chatContainer.scrollTop(chatContainer[0].scrollHeight);
                self.notifyUserFriend(userID, message);
                $(this).val('');
                var nTop = (wrapper.height()*-1);
                wrapper.css({ top : nTop });
            };
        });
        close.click(function(){ wrapper.remove(); });
        content.append(chatContainer).append(chatBox);
        header.append(title).append(close);
        wrapper.append(arrow).append(header).append(content);
        return wrapper;
    };

    /*********************
    *** HANDLE METHODS ***
    *********************/

    /**
     * @method renderChatWrapper
     * @param wrapper
     */
    this.renderChatWrapper = function(wrapper) {
        wrapper.draggable({ axis : 'x', containment : 'body' }).css({
            position : 'absolute',
            top      : '-106px'
        });
        $('#footer').prepend(wrapper);
        return wrapper;
    };

    /**
     * @method handleNotifyUserFriend
     * @param data
     * Handle incoming notification
     */
    this.handleNotifyUserFriend = function(data) {
        //Get chat wrapper
        var wrapper = self.getChatWrapper(data.pk);
        if(!wrapper) {
            wrapper = self.renderChatWrapper(self.setChatWrapper(data.fullName, data.pk));
        };
        //Add message to chatContainer
        var chatContainer = wrapper.find('.chatContainer');
        chatContainer.append($('<p />').text(data.fullName + ' : ' + data.message));
        chatContainer.scrollTop(chatContainer[0].scrollHeight);
        var nTop = (wrapper.height()*-1);
        wrapper.css({ top : nTop });
    };

    /*********************
    *** UPDATE METHODS ***
    *********************/

    /**
     * @method updateUserFriendStatus
     * @param friendList
     */
    this.updateUserFriendStatus = function(friendList) {
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
     * @method updateUserFriendList
     * (Re)render userFriend list
     */
    this.updateUserFriendList = function() {
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
            self.validateUserFriendStatus();
        });
    };

};


/**
 * Load when DOM is ready
 */
$().ready(function(){
    var chat = new StudeBookChat();
    chat.init();
});


