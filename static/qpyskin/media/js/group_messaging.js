var HideableWidget = function() {
    Widget.call(this);
};
inherits(HideableWidget, Widget);

HideableWidget.prototype.setState = function(state) {
    this._state = state;
    if (this._element) {
        if (state === 'shown') {
            this._element.show();
        } else if (state === 'hidden') {
            this._element.hide();
        }
    }
};

HideableWidget.prototype.onAfterShow = function() {};

HideableWidget.prototype.show = function() {
    this.setState('shown');
    this.onAfterShow();
};

HideableWidget.prototype.hide = function() {
    this.setState('hidden');
};

HideableWidget.prototype.decorate = function(element) {
    this._element = element;
};

/**
 * @constructor
 */
var MessageComposer = function() {
    HideableWidget.call(this);
};
inherits(MessageComposer, HideableWidget);

MessageComposer.prototype.onAfterCancel = function(handler) {
    if (handler) {
        this._onAfterCancel = handler;
    } else {
        return this._onAfterCancel();
    }
};

/** override these two 
 * @param {object} data - the response data
 * these functions will run after .send() receives
 * the response
 */
MessageComposer.prototype.onSendSuccessInternal = function(data) {};
MessageComposer.prototype.onSendErrorInternal = function(data) {};

MessageComposer.prototype.onSendSuccess = function(callback) {
    if (callback) {
        this._onSendSuccess = callback;
    } else if (this._onSendSuccess) {
        this._onSendSuccess();
    }
};

MessageComposer.prototype.onSendError = function(callback) {
    if (callback) {
        this._onSendError = callback;
    } else if (this._onSendError) {
        this._onSendError();
    }
};

MessageComposer.prototype.onAfterShow = function() {
    this._textarea.focus();
};

MessageComposer.prototype.cancel = function() {
    this._textarea.val('');
    this._textareaError.html('');
    this.hide();
    this.onAfterCancel();
};

MessageComposer.prototype.setPostData = function(data) {
    this._postData = data;
};

MessageComposer.prototype.getPostData = function() {
    return this._postData;
};

MessageComposer.prototype.setSendUrl = function(url) {
    this._sendUrl = url;
};

MessageComposer.prototype.getInputData = function() {
    return {'text': this._textarea.val()};
};

MessageComposer.prototype.dataIsValid = function() {
    var text = $.trim(this._textarea.val());
    if (text === '') {
        this._textareaError.html(gettext('required'));
        return false;
    }
    return true;
};

MessageComposer.prototype.send = function() {
    var url = this._sendUrl;
    var data = this.getPostData() || {};
    var inputData = this.getInputData();
    $.extend(data, inputData);
    var me = this;
    data['text'] = this._textarea.val();
    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: url,
        data: data,
        cache: false,
        success: function(data) {
            if (data['success']) {
                me.onSendSuccessInternal(data);
                me.onSendSuccess();
            } else {
                me.onSendErrorInternal(data);
                me.onSendError();
            }
        }
    });
};

MessageComposer.prototype.createDom = function() {
    this._element = this.makeElement('div');
    this.hide();
    this._element.addClass('message-composer');
    //create textarea
    var label = this.makeElement('label');
    label.html(gettext('Your message:'));
    this._element.append(label);
    var error = this.makeElement('label');
    error.addClass('errors');
    this._element.append(error);
    this._element.append($('<br/>'));
    this._textareaError = error;
    var textarea = this.makeElement('textarea');
    this._element.append(textarea);
    this._textarea = textarea;
    //send button
    var me = this;
    var sendBtn = this.makeButton(
                        gettext('send'),
                        function() {
                            if (me.dataIsValid()){
                                me.send();
                            }
                        }
                    );
    sendBtn.addClass('submit');
    this._element.append(sendBtn);

    //cancel button
    var cancelBtn = this.makeButton(
                        gettext('cancel'),
                        function() { me.cancel(); }
                    );
    cancelBtn.addClass('submit');
    this._element.append(cancelBtn);
};


var ReplyMessageComposer = function() {
    MessageComposer.call(this);
};
inherits(ReplyMessageComposer, MessageComposer);

ReplyMessageComposer.prototype.setParent = function(elem) {
    this._parent = elem;
};

ReplyMessageComposer.prototype.onSendSuccessInternal = function(data) {
    var message = new Message();
    message.decorate($(data['html']));
    this._parent.addMessage(message);
};

/**
 * @constructor
 * same as message composer, but initially
 * hidden and presented by a "reply" link
 */
var ReplyComposer = function() {
    HideableWidget.call(this);
};
inherits(ReplyComposer, HideableWidget);

ReplyComposer.prototype.open = function() {
    this._opener.hide();
    this._editor.show();
};

ReplyComposer.prototype.close = function() {
    this._opener.show();
    this._editor.hide();
}

ReplyComposer.prototype.setSendUrl = function(url) {
    this._sendUrl = url;
};

ReplyComposer.prototype.setPostData = function(data) {
    this._editor.setPostData(data);
};

ReplyComposer.prototype.setThread = function(thread) {
    this._thread = thread;
};

ReplyComposer.prototype.addMessage = function(message) {
    this._thread.addMessage(message);
};

ReplyComposer.prototype.createDom = function() {
    this._element = this.makeElement('div');
    this._element.addClass('reply-composer');
    var opener = this.makeElement('a');
    opener.html(gettext('Reply'));
    this._opener = opener;
    this._element.append(opener);

    var editor = new ReplyMessageComposer();
    editor.setSendUrl(this._sendUrl);
    editor.setParent(this);
    editor.onSendSuccess(function() {
        editor.cancel();
        notify.show(gettext('message sent'), true);
    });
    this._editor = editor;
    this._element.append(editor.getElement());

    var me = this;
    setupButtonEventHandlers(opener, function() { me.open() });
    editor.onAfterCancel(function() { me.close() });
    this.hide();
};


/**
 * @constructor
 */
var NewThreadComposer = function() {
    MessageComposer.call(this);
};
inherits(NewThreadComposer, MessageComposer);

NewThreadComposer.prototype.cancel = function() {
    this._toInput.val('');
    this._toInputError.html('');
    NewThreadComposer.superClass_.cancel.call(this);
};

NewThreadComposer.prototype.onAfterShow = function() {
    this._toInput.focus();
};

NewThreadComposer.prototype.onSendErrorInternal = function(data) {
    var missingUsers = data['missing_users']
    if (missingUsers) {
        var errorTpl = ngettext(
                            'user {{str}} does not exist',
                            'users {{str}} do not exist',
                            missingUsers.length
                        )
        error = errorTpl.replace('{{str}}', joinAsPhrase(missingUsers));
        this._toInputError.html(error);
    }
};

NewThreadComposer.prototype.getInputData = function() {
    var data = NewThreadComposer.superClass_.getInputData.call(this);
    data['to_usernames'] = $.trim(this._toInput.val());
    return data;
};

NewThreadComposer.prototype.dataIsValid = function() {
    var superIsValid = NewThreadComposer.superClass_.dataIsValid.call(this);
    var to = $.trim(this._toInput.val());
    if (to === '') {
        this._toInputError.html(gettext('required'));
        return false;
    }
    return superIsValid;
};

NewThreadComposer.prototype.createDom = function() {
    NewThreadComposer.superClass_.createDom.call(this);
    var element = this.getElement();

    var toInput = this.makeElement('input');
    toInput.addClass('recipients');
    element.prepend(toInput);
    this._toInput = toInput;

    var userSelectHandler = function() {};

    var usersAc = new AutoCompleter({
        url: '/get-users-info/',//askbot['urls']['get_users_info'],
        preloadData: false,
        minChars: 1,
        useCache: true,
        matchInside: true,
        maxCacheLength: 100,
        delay: 10,
        onItemSelect: userSelectHandler
    });

    usersAc.decorate(toInput);

    var label = this.makeElement('label');
    label.html(gettext('Recipient:'));
    element.prepend(label);
    var error = this.makeElement('label');
    this._element.append($('<br/>'));
    error.addClass('errors');
    this._toInputError = error;
    label.after(error);
};

var ThreadHeading = function() {
    SimpleControl.call(this);
};
inherits(ThreadHeading, SimpleControl);

ThreadHeading.prototype.getId = function() {
    return this._id;
};

ThreadHeading.prototype.decorate = function(element) {
    this._element = element;
    this._id = element.data('threadId');
};

/**
 * @constructor
 */
var ThreadsList = function() {
    HideableWidget.call(this);
};
inherits(ThreadsList, HideableWidget);

ThreadsList.prototype.setMessageCenter = function(ctr) {
    this._messageCenter = ctr;
};

ThreadsList.prototype.getOpenThreadHandler = function(threadId) {
    var messageCenter = this._messageCenter;
    return function() {
        messageCenter.openThread(threadId);
    };
};

ThreadsList.prototype.setHTML = function(html) {
    $.each(this._threads, function(idx, thread) {
        thread.dispose();
    });
    this._element.html(html);
    this.decorate(this._element);
};

ThreadsList.prototype.decorate = function(element) {
    this._element = element;
    var headingElements = element.find('tr.thread-heading');
    var me = this;
    var threads = [];
    $.each(headingElements, function(idx, headingElement) {
        var heading = new ThreadHeading();
        heading.decorate($(headingElement));
        var threadId = heading.getId();
        heading.setHandler(me.getOpenThreadHandler(threadId));
        threads.push(heading);
    });
    this._threads = threads;
}


/**
 * @constructor
 */
var Message = function() {
    Widget.call(this);
};
inherits(Message, Widget);

Message.prototype.getId = function() {
    return this._id;
};

Message.prototype.decorate = function(element) {
    this._element = element;
    this._id = element.data('messageId');
};


/**
 * @constructor
 */
var ThreadContainer = function() {
    HideableWidget.call(this);
};
inherits(ThreadContainer, HideableWidget);

ThreadContainer.prototype.show = function() {
    ThreadContainer.superClass_.show.call(this);
    this._editor.close();
    this._editor.show();
};

ThreadContainer.prototype.hide = function() {
    ThreadContainer.superClass_.hide.call(this);
    this._editor.close();
    this._editor.hide();
};

/**
 * sets html content part of the thread
 * and re-decorates it
 */
ThreadContainer.prototype.setContent = function(html) {
    if (this._thread) {
        this._thread.dispose();
    }
    var thread = new Thread();
    thread.decorate($(html));
    this._thread = thread;
    this._contentElement.empty();
    this._contentElement.append(thread.getElement());
    var postData = {parent_id: thread.getLastMessageId()};
    this._editor.setPostData(postData);
    this._editor.setThread(thread);
};

ThreadContainer.prototype.setReplyUrl = function(url) {
    this._replyUrl = url;
};

ThreadContainer.prototype.createDom = function() {
    this._element = this.makeElement('div');
    var content = this.makeElement('div');
    this._contentElement = content;
    this._element.append(content);

    var editor = new ReplyComposer();
    editor.setSendUrl(this._replyUrl);
    this._element.append(editor.getElement());
    this._editor = editor;
};


/**
 * @constructor
 */
var Thread = function() {
    WrappedElement.call(this);
};
inherits(Thread, WrappedElement);

Thread.prototype.getLastMessageId = function() {
    return this._messages.slice(-1)[0].getId();
};

Thread.prototype.dispose = function() {
    $.each(this._messages, function(idx, message) {
        message.dispose()
    });
    Thread.superClass_.dispose.call(this);
};

Thread.prototype.addMessage = function(message) {
    var li = this.makeElement('li');
    this._element.append(li);
    li.append(message.getElement());
};

Thread.prototype.decorate = function(element) {
    this._element = element;
    var messages = [];
    $.each(element.find('.message'), function(idx, item) {
        var message = new Message();
        message.decorate($(item));
        messages.push(message);
    });
    this._messages = messages;
};


/**
 * @constructor
 */
var Sender = function() {
    SimpleControl.call(this);
};
inherits(Sender, SimpleControl);

Sender.prototype.getId = function() {
    return this._id;
};

Sender.prototype.select = function() {
    this._element.addClass('selected');
};

Sender.prototype.unselect = function() {
    this._element.removeClass('selected');
};

Sender.prototype.decorate = function(element) {
    Sender.superClass_.decorate.call(this, element);
    this._id = element.data('senderId');
};


/**
 * @constructor
 * list of senders in the first column of inbox
 */
var SendersList = function() {
    WrappedElement.call(this);
    this._messageCenter = undefined;
};
inherits(SendersList, WrappedElement);

SendersList.prototype.setMessageCenter = function(ctr) {
    this._messageCenter = ctr;
};

SendersList.prototype.getSenders = function() {
    return this._senders;
};

SendersList.prototype.getSenderSelectHandler = function(sender) {
    var messageCenter = this._messageCenter;
    var me = this;
    return function() {
        $.map(me.getSenders(), function(s){ s.unselect() });
        sender.select();
        messageCenter.loadThreadsForSender(sender.getId());
    };
};

SendersList.prototype.decorate = function(element) {
    this._element = element;
    var senders = [];
    $.each(element.find('a'), function(idx, item) {
        var sender = new Sender();
        sender.decorate($(item));
        senders.push(sender);
    });

    this._senders = senders;

    var me = this;
    $.each(senders, function(idx, sender) {
        sender.setHandler(me.getSenderSelectHandler(sender));
    });
};


/**
 * @contsructor
 */
var MessageCenter = function() {
    Widget.call(this);
};
inherits(MessageCenter, Widget);

MessageCenter.prototype.setState = function(state) {
    this._editor.hide();
    this._threadsList.hide();
    this._threadContainer.hide();
    if (state === 'compose') {
        this._editor.show();
    } else if (state === 'show-list') {
        this._threadsList.show();
    } else if (state === 'show-thread') {
        this._threadContainer.show();
    }
};

MessageCenter.prototype.openThread = function(threadId) {
    var url = this._urls['getThreads'] + threadId + '/';
    var me = this;
    var threadContainer = this._threadContainer;
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: url,
        cache: false,
        success: function(data) {
            if (data['success']) {
                threadContainer.setContent(data['html']);
                me.setState('show-thread');
            }
        }
    });
};

MessageCenter.prototype.loadThreadsForSender = function(senderId) {
    var threadsList = this._threadsList;
    var url = this._urls['getThreads'];
    me = this;
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: url,
        cache: false,
        data: {sender_id: senderId},
        success: function(data) {
            if (data['success']) {
                threadsList.setHTML(data['html']);
                me.setState('show-list');
            }
        }
    });
};

MessageCenter.prototype.decorate = function(element) {
    this._element = element;
    this._firstCol = element.find('.first-col');
    this._secondCol = element.find('.second-col');

    this._urls = {
        getThreads: element.data('getThreadsUrl'),
        getThreadDetails: element.data('getThreadDetailsUrl'),
        reply: element.data('replyUrl')
    };

    //read sender list
    var senders = new SendersList();
    senders.setMessageCenter(this);
    senders.decorate($('.senders-list'));
    this._sendersList = senders;
    //read message list
    var threads = new ThreadsList();
    threads.setMessageCenter(this);
    threads.decorate($('.threads-list'));
    this._threadsList = threads;
    //add empty thread container
    var threadContainer = new ThreadContainer();
    this._threadContainer = threadContainer;
    threadContainer.setReplyUrl(this._urls['reply']);
    this._secondCol.append(threadContainer.getElement());

    var me = this;
    //create editor
    var editor = new NewThreadComposer();
    this._secondCol.append(editor.getElement());
    editor.setSendUrl(element.data('createThreadUrl'));
    editor.onAfterCancel(function() { me.setState('show-list') });
    editor.onSendSuccess(function() {
        editor.cancel();
        notify.show(gettext('message sent'), true);
    });
    this._editor = editor;

    //activate compose button
    var btn = element.find('button.compose');
    this._composeBtn = btn;
    setupButtonEventHandlers(btn, function(){ me.setState('compose') });
};

var msgCtr = new MessageCenter();
msgCtr.decorate($('.group-messaging'));
