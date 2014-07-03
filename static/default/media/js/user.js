//todo: refactor this into "Inbox" object or more specialized
var setup_inbox = function(){

    var getSelected = function(){

        var id_list = new Array();
        var elements = $('#responses input:checked').parent();

        elements.each(function(index, element){
            var id = $(element).attr('id').replace(/^re_/,'');
            id_list.push(id);
        });

        if (id_list.length === 0){
            alert(gettext('Please select at least one item'));
        }

        return {id_list: id_list, elements: elements};
    };

    var submit = function(id_list, elements, action_type){
        if (action_type == 'delete' || action_type == 'mark_new' || action_type == 'mark_seen' || action_type == 'remove_flag' || action_type == 'delete_post'){
            $.ajax({
                type: 'POST',
                cache: false,
                dataType: 'json',
                data: JSON.stringify({memo_list: id_list, action_type: action_type}),
                url: askbot['urls']['manageInbox'],
                success: function(response_data){
                    if (response_data['success'] == true){
                        if (action_type == 'delete' || action_type == 'remove_flag' || action_type == 'delete_post'){
                            elements.remove();
                        }
                        else if (action_type == 'mark_new'){
                            elements.addClass('highlight');
                            elements.addClass('new');
                            elements.removeClass('seen');
                        }
                        else if (action_type == 'mark_seen'){
                            elements.removeClass('highlight');
                            elements.addClass('seen');
                            elements.removeClass('new');
                        }
                    }
                    else {
                        showMessage($('#responses'), response_data['message']);
                    }
                }
            });
        }
    };

    var startAction = function(action_type){
        var data = getSelected();
        if (data['id_list'].length === 0){
            return;
        }
        if (action_type == 'delete'){
            msg = ngettext('Delete this notification?',
					'Delete these notifications?', data['id_list'].length);
            if (confirm(msg) === false){
                return;
            }
        }
        if (action_type == 'close'){
            msg = ngettext('Close this entry?',
                    'Close these entries?', data['id_list'].length);
            if (confirm(msg) === false){
                return;
            }
        }
        if (action_type == 'remove_flag'){
            msg = ngettext(
                    'Remove all flags and approve this entry?',
                    'Remove all flags and approve these entries?',
                    data['id_list'].length
                );
            if (confirm(msg) === false){
                return;
            }
        }
        submit(data['id_list'], data['elements'], action_type);
    };
    setupButtonEventHandlers($('#re_mark_seen'), function(){startAction('mark_seen')});
    setupButtonEventHandlers($('#re_mark_new'), function(){startAction('mark_new')});
    setupButtonEventHandlers($('#re_dismiss'), function(){startAction('delete')});
    setupButtonEventHandlers($('#re_remove_flag'), function(){startAction('remove_flag')});
    //setupButtonEventHandlers($('#re_close'), function(){startAction('close')});
    setupButtonEventHandlers(
                    $('#sel_all'),
                    function(){
                        setCheckBoxesIn('#responses .new', true);
                        setCheckBoxesIn('#responses .seen', true);
                    }
    );
    setupButtonEventHandlers(
                    $('#sel_seen'),
                    function(){
                        setCheckBoxesIn('#responses .seen', true);
                    }
    );
    setupButtonEventHandlers(
                    $('#sel_new'),
                    function(){
                        setCheckBoxesIn('#responses .new', true);
                    }
    );
    setupButtonEventHandlers(
                    $('#sel_none'),
                    function(){
                        setCheckBoxesIn('#responses .new', false);
                        setCheckBoxesIn('#responses .seen', false);
                    }
    );

    var rejectPostDialog = new RejectPostDialog();
    rejectPostDialog.decorate($('#reject-edit-modal'));
    rejectPostDialog.setSelectedEditDataReader(function(){
        return getSelected();
    });
    setupButtonEventHandlers(
        $('#re_delete_post'),
        function(){
            if (rejectPostDialog.readSelectedEditData()) {
                rejectPostDialog.show();
            }
        }
    );

    if ($('body').hasClass('inbox-flags')) {
        var responses = $('.response-parent');
        responses.each(function(idx, response) {
            var control = new PostModerationControls();
            control.setParent($(response));
            control.setReasonsDialog(rejectPostDialog);
            rejectPostDialog.addPostModerationControl(control);
            $(response).append(control.getElement());
        });
    }
};

var setup_badge_details_toggle = function(){
    $('.badge-context-toggle').each(function(idx, elem){
        var context_list = $(elem).parent().next('ul');
        if (context_list.children().length > 0){
            $(elem).addClass('active');
            var toggle_display = function(){
                if (context_list.css('display') == 'none'){
                    $('.badge-context-list').hide();
                    context_list.show();
                } else {
                    context_list.hide();
                }
            };
            $(elem).click(toggle_display);
        }
    });
};

var PostModerationControls = function() {
    WrappedElement.call(this);
};
inherits(PostModerationControls, WrappedElement);

PostModerationControls.prototype.setParent = function(parent_element) {
    this._parent_element = parent_element;
};

PostModerationControls.prototype.setReasonsDialog = function(dialog) {
    this._reasonsDialog = dialog;
};

PostModerationControls.prototype.getMemoId = function() {
    return this._parent_element.data('responseId');
};

PostModerationControls.prototype.getMemoElement = function() {
    var reId = this.getMemoId();
    return $('#re_' + reId);
};

PostModerationControls.prototype.removeMemo = function() {
    this.getMemoElement().remove();
};

PostModerationControls.prototype.markMemo = function() {
    var memo = this.getMemoElement();
    var checkbox = memo.find('input[type="checkbox"]');
    checkbox.attr('checked', true);
};

PostModerationControls.prototype.addReason = function(id, title) {
    var li = this.makeElement('li');
    var anchor = this.makeElement('a');
    anchor.html(title);
    anchor.data('postId', id);
    li.append(anchor);
    var adderLink = this._reasonList.children().last();
    adderLink.before(li);
    //attach event handler
    var me = this;
    setupButtonEventHandlers(anchor, function() { me.moderatePost(id, 'delete_post') });
};

PostModerationControls.prototype.moderatePost = function(reasonId, actionType){
    var me = this;
    var data = {
        reject_reason_id: reasonId,
        memo_list: [me.getMemoId()],
        action_type: actionType
    };
    $.ajax({
        type: 'POST',
        dataType: 'json',
        cache: false,
        data: JSON.stringify(data),
        url: askbot['urls']['manageInbox'],
        success: function(data){
            if (data['success']){
                me.removeMemo();
                me.dispose();
                if (actionType === 'delete') {
                    notify.show(gettext('Post deleted'));
                } else if (actionType === 'remove_flag') {
                    notify.show(gettext('Post approved'));
                }
            } else {
                notify.show(data['message']);
            }
        }
    });
};


PostModerationControls.prototype.createDom = function() {
    var toolbar = this.makeElement('div');
    toolbar.addClass('btn-toolbar post-moderation-controls');
    this._element = toolbar;

    var div = this.makeElement('div');
    div.addClass('btn-group');
    toolbar.append(div);

    var acceptBtn = this.makeElement('a');
    acceptBtn.addClass('btn save-reason');
    acceptBtn.html(gettext('Accept'));
    div.append(acceptBtn);

    div = this.makeElement('div');
    div.addClass('btn-group dropdown');
    toolbar.append(div);

    var toggle = this.makeElement('button');
    toggle.addClass('btn btn-danger dropdown-toggle');
    toggle.append($('<span>' + gettext('Reject') + '</span>'));
    toggle.append($('<span class="caret"></span>'));
    div.append(toggle);

    toggle.dropdown();

    var ul = this.makeElement('ul');
    ul.addClass('dropdown-menu');
    div.append(ul);

    this._reasonList = ul;

    //reason adder
    var li = this.makeElement('li');
    var anchor = this.makeElement('a');
    anchor.html(gettext('add new reject reason'));
    li.append(anchor);
    ul.append(li);

    //append menu items
    var me = this;
    $.each(askbot['data']['postRejectReasons'], function(idx, reason) {
        me.addReason(reason['id'], reason['title']);
    });

    var reasonsDlg = this._reasonsDialog;
    setupButtonEventHandlers(anchor, function() {
        me.markMemo();//mark current post
        reasonsDlg.readSelectedEditData();//read data of selected edits
        reasonsDlg.show();//open the "big" dialog
    });
    setupButtonEventHandlers(acceptBtn, function() { 
        me.moderatePost(null, 'remove_flag');
    });
};

/**
 * @constructor
 * manages post/edit reject reasons
 * in the post moderation view
 */
var RejectPostDialog = function(){
    WrappedElement.call(this);
    this._selected_edit_ids = null;
    this._selected_reason_id = null;
    this._state = null;//'select', 'preview', 'add-new'
    this._postModerationControls = [];
    this._selectedEditDataReader = undefined;
};
inherits(RejectPostDialog, WrappedElement);

RejectPostDialog.prototype.setSelectedEditDataReader = function(func) {
    this._selectedEditDataReader = func;
};

RejectPostDialog.prototype.readSelectedEditData = function() {
    var data = this._selectedEditDataReader();
    this.setSelectedEditData(data);
    return data['id_list'].length > 0;
};

RejectPostDialog.prototype.setSelectedEditData = function(data){
    this._selected_edit_data = data;
};

RejectPostDialog.prototype.addPostModerationControl = function(control) {
    this._postModerationControls.push(control);
};

RejectPostDialog.prototype.setState = function(state){
    this._state = state;
    this.clearErrors();
    if (this._element){
        this._selector.hide();
        this._adder.hide();
        this._previewer.hide();
        if (state === 'select'){
            this._selector.show();
        } else if (state === 'preview'){
            this._previewer.show();
        } else if (state === 'add-new'){
            this._adder.show();
        }
    }
};

RejectPostDialog.prototype.show = function(){
    $(this._element).modal('show');
};

RejectPostDialog.prototype.hide = function(){
    $(this._element).modal('hide');
};

RejectPostDialog.prototype.resetInputs = function(){
    if (this._title_input){
        this._title_input.reset();
    }
    if (this._details_input){
        this._details_input.reset();
    }
    var selected = this._element.find('.selected');
    selected.removeClass('selected');
};

RejectPostDialog.prototype.clearErrors = function(){
    var error = this._element.find('.alert');
    error.remove();
};

RejectPostDialog.prototype.makeAlertBox = function(errors){
    //construct the alert box
    var alert_box = new AlertBox();
    alert_box.setClass('alert-error');
    if (typeof errors === "string"){
        alert_box.setText(errors);
    } else if (errors.constructor === [].constructor){
        if (errors.length > 1){
            alert_box.setContent(
                '<div>' + 
                gettext('Looks there are some things to fix:') +
                '</div>'
            )
            var list = this.makeElement('ul');
            $.each(errors, function(idx, item){
                list.append('<li>' + item + '</li>');
            });
            alert_box.addContent(list);
        } else if (errors.length == 1){
            alert_box.setContent(errors[0]);
        } else if (errors.length == 0){
            return;
        }
    } else if ('html' in errors){
        alert_box.setContent(errors);
    } else {
        return;//don't know what to do
    }
    return alert_box;
};

RejectPostDialog.prototype.setAdderErrors = function(errors){
    //clear previous errors
    this.clearErrors();
    var alert_box = this.makeAlertBox(errors);
    this._element
        .find('#reject-edit-modal-add-new .modal-body')
        .prepend(alert_box.getElement());
};

RejectPostDialog.prototype.setSelectorErrors = function(errors){
    this.clearErrors();
    var alert_box = this.makeAlertBox(errors);
    this._element
        .find('#reject-edit-modal-select .modal-body')
        .prepend(alert_box.getElement());
};

RejectPostDialog.prototype.setErrors = function(errors){
    this.clearErrors();
    var alert_box = this.makeAlertBox(errors);
    var current_state = this._state;
    this._element
        .find('#reject-edit-modal-' + current_state + ' .modal-body')
        .prepend(alert_box.getElement());
};

RejectPostDialog.prototype.addSelectableReason = function(data){
    var id = data['reason_id'];
    var title = data['title'];
    var details = data['details'];
    this._select_box.addItem(id, title, details);

    askbot['data']['postRejectReasons'].push(
        {id: data['reason_id'], title: data['title']}
    );
    $.each(this._postModerationControls, function(idx, control) {
        control.addReason(data['reason_id'], data['title']);
    });
};

RejectPostDialog.prototype.startSavingReason = function(callback){

    var title_input = this._title_input;
    var details_input = this._details_input;

    var errors = [];
    if (title_input.isBlank()){
        errors.push(gettext('Please provide description.'));
    }
    if (details_input.isBlank()){
        errors.push(gettext('Please provide details.'));
    }

    if (errors.length > 0){
        this.setAdderErrors(errors);
        return;//just show errors and quit
    }

    var data = {
        title: title_input.getVal(),
        details: details_input.getVal()
    };
    if (this._selected_reason_id){
        data['reason_id'] = this._selected_reason_id;
    }

    var me = this;

    $.ajax({
        type: 'POST',
        dataType: 'json',
        cache: false,
        url: askbot['urls']['save_post_reject_reason'],
        data: data,
        success: function(data){
            if (data['success']){
                //show current reason data and focus on it
                me.addSelectableReason(data);
                if (callback){
                    callback(data);
                } else {
                    me.setState('select');
                }
            } else {
                me.setAdderErrors(data['message']);
            }
        }
    });
};

RejectPostDialog.prototype.rejectPost = function(reason_id){
    var me = this;
    var memos = this._selected_edit_data['elements'];
    var memo_ids = this._selected_edit_data['id_list'];
    var data = {
        reject_reason_id: reason_id,
        memo_list: memo_ids,
        action_type: 'delete_post'
    };
    $.ajax({
        type: 'POST',
        dataType: 'json',
        cache: false,
        data: JSON.stringify(data),
        url: askbot['urls']['manageInbox'],
        success: function(data){
            if (data['success']){
                $.each(memos, function(idx, memo) {
                    $(memo).next('.post-moderation-controls').remove();
                    $(memo).remove();
                });
                me.hide();
            } else {
                //only fatal errors here
                me.setErrors(data['message']);
            }
        }
    });
};

RejectPostDialog.prototype.setPreviewerData = function(data){
    this._selected_reason_id = data['id'];
    this._element.find('.selected-reason-title').html(data['title']);
    this._element.find('.selected-reason-details').html(data['details']);
};

RejectPostDialog.prototype.startEditingReason = function(){
    var title = this._element.find('.selected-reason-title').html();
    var details = this._element.find('.selected-reason-details').html();
    this._title_input.setVal(title);
    this._details_input.setVal(details);
    this.setState('add-new');
};

RejectPostDialog.prototype.resetSelectedReasonId = function(){
    this._selected_reason_id = null;
};

RejectPostDialog.prototype.getSelectedReasonId = function(){
    return this._selected_reason_id;
};

RejectPostDialog.prototype.startDeletingReason = function(){
    var select_box = this._select_box;
    var data = select_box.getSelectedItemData();
    var reason_id = data['id'];
    var me = this;
    if (data['id']){
        $.ajax({
            type: 'POST',
            dataType: 'json',
            cache: false,
            url: askbot['urls']['delete_post_reject_reason'],
            data: {reason_id: reason_id},
            success: function(data){
                if (data['success']){
                    select_box.removeItem(reason_id);
                } else {
                    me.setSelectorErrors(data['message']);
                }
            }
        });
    } else {
        me.setSelectorErrors(
            gettext('A reason must be selected to delete one.')
        )
    }
};

RejectPostDialog.prototype.decorate = function(element){
    this._element = element;
    //set default state according to the # of available reasons
    this._selector = $(element).find('#reject-edit-modal-select');
    this._adder = $(element).find('#reject-edit-modal-add-new');
    this._previewer = $(element).find('#reject-edit-modal-preview');
    if (this._selector.find('li').length > 0){
        this.setState('select');
        this.resetInputs();
    } else {
        this.setState('add-new');
        this.resetInputs();
    }

    $(this._element).find('.dropdown-toggle').dropdown();

    var select_box = new SelectBox();
    select_box.decorate($(this._selector.find('.select-box')));
    this._select_box = select_box;

    //setup tipped-inputs
    var reject_title_input = $(this._element).find('input');
    var title_input = new TippedInput();
    title_input.decorate($(reject_title_input));
    this._title_input = title_input;

    var reject_details_input = $(this._element)
        .find('textarea.reject-reason-details');

    var details_input = new TippedInput();
    details_input.decorate($(reject_details_input));
    this._details_input = details_input;

    var me = this;
    setupButtonEventHandlers(
        element.find('.cancel, .modal-header .close'),
        function() {
            me.hide();
            me.clearErrors();
            me.resetInputs();
            me.resetSelectedReasonId();
            me.setState('select');
        }
    );

    setupButtonEventHandlers(
        $(this._element).find('.save-reason'),
        function(){ me.startSavingReason() }
    );

    setupButtonEventHandlers(
        $(this._element).find('.save-reason-and-reject'),
        function(){
            me.startSavingReason(
                function(data){
                    me.rejectPost(data['reason_id']);
                }
            );
        }
    );

    setupButtonEventHandlers(
        $(this._element).find('.reject'),
        function(){
            me.rejectPost(me.getSelectedReasonId());
        }
    );

    setupButtonEventHandlers(
        element.find('.select-other-reason'),
        function(){ 
            me.resetInputs();
            me.setState('select');
        }
    )

    setupButtonEventHandlers(
        element.find('.add-new-reason'),
        function(){ 
            me.resetSelectedReasonId();
            me.resetInputs();
            me.setState('add-new') 
        }
    );

    setupButtonEventHandlers(
        element.find('.select-this-reason'),
        function(){
            var data = select_box.getSelectedItemData();
            if (data['id']){
                me.setState('preview');
                me.setPreviewerData(data);
            } else {
                me.setSelectorErrors(
                    gettext('A reason must be selected to reject post.')
                )
            }
        }
    );

    setupButtonEventHandlers(
        element.find('.edit-reason'),
        function(){
            me.startEditingReason();
        }
    );

    setupButtonEventHandlers(
        element.find('.delete-this-reason'),
        function(){
            me.startDeletingReason();
        }
    )
};

/**
 * @constructor
 * allows to follow/unfollow users
 */
var FollowUser = function(){
    WrappedElement.call(this);
    this._user_id = null;
    this._user_name = null;
};
inherits(FollowUser, WrappedElement);

/**
 * @param {string} user_name
 */
FollowUser.prototype.setUserName = function(user_name){
    this._user_name = user_name;
};

FollowUser.prototype.decorate = function(element){
    this._element = element;
    this._user_id = parseInt(element.attr('id').split('-').pop());
    this._available_action = element.children().hasClass('follow') ? 'follow':'unfollow';
    var me = this;
    setupButtonEventHandlers(this._element, function(){ me.go() });
};

FollowUser.prototype.go = function(){
    if (askbot['data']['userIsAuthenticated'] === false){
        var message = gettext('Please <a href="%(signin_url)s">signin</a> to follow %(username)s');
        var message_data = {
            signin_url: askbot['urls']['user_signin'] + '?next=' + window.location.href,
            username: this._user_name
        }
        message = interpolate(message, message_data, true);
        showMessage(this._element, message);
        return;
    }
    var user_id = this._user_id;
    if (this._available_action === 'follow'){
        var url = askbot['urls']['follow_user'];
    } else {
        var url = askbot['urls']['unfollow_user'];
    }
    var me = this;
    $.ajax({
        type: 'POST',
        cache: false,
        dataType: 'json',
        url: url.replace('{{userId}}', user_id),
        success: function(){ me.toggleState() }
    });
};

FollowUser.prototype.toggleState = function(){
    if (this._available_action === 'follow'){
        this._available_action = 'unfollow';
        var unfollow_div = document.createElement('div'); 
        unfollow_div.setAttribute('class', 'unfollow');
        var red_div = document.createElement('div');
        red_div.setAttribute('class', 'unfollow-red');
        red_div.innerHTML = interpolate(gettext('unfollow %s'), [this._user_name]);
        var green_div = document.createElement('div');
        green_div.setAttribute('class', 'unfollow-green');
        green_div.innerHTML = interpolate(gettext('following %s'), [this._user_name]);
        unfollow_div.appendChild(red_div);
        unfollow_div.appendChild(green_div);
        this._element.html(unfollow_div);
    } else {
        var follow_div = document.createElement('div'); 
        follow_div.innerHTML = interpolate(gettext('follow %s'), [this._user_name]);
        follow_div.setAttribute('class', 'follow');
        this._available_action = 'follow';
        this._element.html(follow_div);
    }
};

/**
 * @constructor
 * @param {string} name
 */
var UserGroup = function(name){
    WrappedElement.call(this);
    this._name = name;
    this._content = null;
};
inherits(UserGroup, WrappedElement);

UserGroup.prototype.getDeleteHandler = function(){
    var group_name = this._name;
    var me = this;
    var groups_container = me._groups_container;
    return function(){
        var data = {
            user_id: askbot['data']['viewUserId'],
            group_name: group_name,
            action: 'remove'
        };
        $.ajax({
            type: 'POST',
            dataType: 'json',
            data: data,
            cache: false,
            url: askbot['urls']['edit_group_membership'],
            success: function(){
                groups_container.removeGroup(me);
            }
        });
    };
};

UserGroup.prototype.setContent = function(content){
    this._content = content;
};

UserGroup.prototype.getName = function(){
    return this._name;
};

UserGroup.prototype.setGroupsContainer = function(container){
    this._groups_container = container;
};

UserGroup.prototype.decorate = function(element){
    this._element = element;
    this._name = $.trim(element.find('a').html());
    var deleter = new DeleteIcon();
    deleter.setHandler(this.getDeleteHandler());
    deleter.setContent(gettext('Remove'));
    this._element.find('td:last').append(deleter.getElement());
    this._delete_icon = deleter;
};

UserGroup.prototype.createDom = function(){
    var element = this.makeElement('tr');
    element.html(this._content);
    this._element = element;
    this.decorate(element);
};

UserGroup.prototype.dispose = function(){
    this._delete_icon.dispose();
    this._element.remove();
};

/**
 * @constructor
 */
var GroupsContainer = function(){
    WrappedElement.call(this);
};
inherits(GroupsContainer, WrappedElement);

GroupsContainer.prototype.decorate = function(element){
    this._element = element;
    var groups = [];
    var group_names = [];
    var me = this;
    //collect list of groups
    $.each(element.find('tr'), function(idx, li){
        var group = new UserGroup();
        group.setGroupsContainer(me);
        group.decorate($(li));
        groups.push(group);
        group_names.push(group.getName());
    });
    this._groups = groups;
    this._group_names = group_names;
};

GroupsContainer.prototype.addGroup = function(group_data){
    var group_name = group_data['name'];
    if ($.inArray(group_name, this._group_names) > -1){
        return;
    }
    var group = new UserGroup(group_name);
    group.setContent(group_data['html']);
    group.setGroupsContainer(this);
    this._groups.push(group);
    this._group_names.push(group_name);
    this._element.append(group.getElement());
};

GroupsContainer.prototype.removeGroup = function(group){
    var idx = $.inArray(group, this._groups);    
    if (idx === -1){
        return;
    }
    this._groups.splice(idx, 1);
    this._group_names.splice(idx, 1);
    group.dispose();
};

var GroupAdderWidget = function(){
    WrappedElement.call(this);
    this._state = 'display';//display or edit
};
inherits(GroupAdderWidget, WrappedElement);

/**
 * @param {string} state
 */
GroupAdderWidget.prototype.setState = function(state){
    if (state === 'display'){
        this._element.html(gettext('add group'));
        this._input.hide();
        this._input.val('');
        this._button.hide();
    } else if (state === 'edit'){
        this._element.html(gettext('cancel'));
        this._input.show();
        this._input.focus();
        this._button.show();
    } else {
        return;
    }
    this._state = state;
};

GroupAdderWidget.prototype.getValue = function(){
    return this._input.val();
};

GroupAdderWidget.prototype.addGroup = function(group_data){
    this._groups_container.addGroup(group_data);
};

GroupAdderWidget.prototype.getAddGroupHandler = function(){
    var me = this;
    return function(){
        var group_name = me.getValue();
        var data = {
            group_name: group_name,
            user_id: askbot['data']['viewUserId'],
            action: 'add'
        };
        $.ajax({
            type: 'POST',
            dataType: 'json',
            data: data,
            cache: false,
            url: askbot['urls']['edit_group_membership'],
            success: function(data){
                if (data['success'] == true){
                    me.addGroup(data);
                    me.setState('display');
                } else {
                    var message = data['message'];
                    showMessage(me.getElement(), message, 'after');
                }
            }
        });
    };
};

GroupAdderWidget.prototype.setGroupsContainer = function(container){
    this._groups_container = container;
};

GroupAdderWidget.prototype.toggleState = function(){
    if (this._state === 'display'){
        this.setState('edit');
    } else if (this._state === 'edit'){
        this.setState('display');
    }
};

GroupAdderWidget.prototype.decorate = function(element){
    this._element = element;
    var input = this.makeElement('input');
    this._input = input;

    var groupsAc = new AutoCompleter({
        url: askbot['urls']['getGroupsList'],
        preloadData: true,
        minChars: 1,
        useCache: false,
        matchInside: false,
        maxCacheLength: 100,
        delay: 10
    });
    groupsAc.decorate(input);

    var button = this.makeElement('button');
    button.html(gettext('add'));
    this._button = button;
    element.before(input);
    input.after(button);
    this.setState('display');
    setupButtonEventHandlers(button, this.getAddGroupHandler());
    var me = this;
    setupButtonEventHandlers(
        element,
        function(){ me.toggleState() }
    );
};

/**
 * @constructor
 * allows editing user groups
 */
var UserGroupsEditor = function(){
    WrappedElement.call(this);
};
inherits(UserGroupsEditor, WrappedElement);

UserGroupsEditor.prototype.decorate = function(element){
    this._element = element;
    var add_link = element.find('#add-group');
    var adder = new GroupAdderWidget();
    adder.decorate(add_link);

    var groups_container = new GroupsContainer();
    groups_container.decorate(element.find('#groups-list'));
    adder.setGroupsContainer(groups_container);
    //todo - add group deleters
};

(function(){
    var fbtn = $('.follow-user-toggle');
    if (fbtn.length === 1){
        var follow_user = new FollowUser();
        follow_user.decorate(fbtn);
        follow_user.setUserName(askbot['data']['viewUserName']);
    }
    if (askbot['data']['userId'] !== askbot['data']['viewUserId']) {
        if (askbot['data']['userIsAdminOrMod']){
            var group_editor = new UserGroupsEditor();
            group_editor.decorate($('#user-groups'));
        } else {
            $('#add-group').remove();
        }
    } else {
        $('#add-group').remove();
    }
})();
