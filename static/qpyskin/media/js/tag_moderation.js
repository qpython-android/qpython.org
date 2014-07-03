/**
 * @constructor
 * base class for two tag moderators - per thread
 * and per tag
 */
var TagModerator = function() {
    WrappedElement.call(this);
    this._tagId = undefined;
    this._threadId = undefined;
};
inherits(TagModerator, WrappedElement);

TagModerator.prototype.setTagId = function(id) {
    this._tagId = id;
};

TagModerator.prototype.getTagId = function() {
    return this._tagId;
};

TagModerator.prototype.setThreadId = function(id) {
    this._threadId = id;
};

TagModerator.prototype.getThreadId = function() {
    return this._threadId;
};

TagModerator.prototype.afterActionHandler = function() {
    throw "Implement me";
};

/**
 * @return {function}
 * the returned function makes an ajax post
 * to the moderate tag url. thread id is added
 * as parameter to data, if defined.
 */
TagModerator.prototype.getHandler = function(action) {
    var me = this;
    return function() {
        var data = {
            action: action,
            tag_id: me.getTagId()
        };
        if (me.getThreadId() !== undefined) {
            data['thread_id'] = me.getThreadId();
        }
        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: askbot['urls']['moderateSuggestedTag'],
            cache: false,
            data: data,
            success: function(data) {
                if (data['success']) {
                    $(me.getElement()).fadeOut();
                    me.afterActionHandler();
                } else {
                    showMessage($(me.getElement()), data['error']);
                }
            }
        });
    };
};
/**
 * @constructor
 */
var PerThreadTagModerator = function() {
    TagModerator.call(this);
    this._tagId = undefined;
    this._threadId = undefined;
    this._parent = undefined;
};
inherits(PerThreadTagModerator, TagModerator);

PerThreadTagModerator.prototype.setParent = function(thing) {
    this._parent = thing;
};

PerThreadTagModerator.prototype.afterActionHandler = function() {
    var ancestor = this._parent;
    ancestor.removeChild(this);
    var childCount = ancestor.getChildCount();
    if (childCount == 1) {
        ancestor.hideButtons();
        this.dispose();
    } else if (childCount == 0) {
        var table = $('.suggested-tags-table');
        table.before($('<p>' + gettext('No suggested tags left') + '</p>'));
        table.remove();
        ancestor.dispose();
    } else {
        this.dispose();
    }
};

PerThreadTagModerator.prototype.decorate = function(element) {
    this._element = element;
    this._threadId = element.data('threadId');

    var acceptBtn = element.find('button.accept');
    var rejectBtn = element.find('button.reject');

    var mouseEnterHandler = function() {
        acceptBtn.fadeIn('fast');
        rejectBtn.fadeIn('fast');
        return false;
    };
    var mouseLeaveHandler = function() {
        acceptBtn.stop().hide();
        rejectBtn.stop().hide();
        return false;
    };

    element.mouseenter(mouseEnterHandler);
    element.mouseleave(mouseLeaveHandler);

    setupButtonEventHandlers(acceptBtn, this.getHandler('accept'));
    setupButtonEventHandlers(rejectBtn, this.getHandler('reject'));
    //threadInfo.hover(mouseEnterHandler, mouseLeaveHandler);
    //element.hover(mouseEnterHandler, mouseLeaveHandler);
};

/**
 * @constructor
 */
var AllThreadsTagModerator = function() {
    TagModerator.call(this);
    this._tag_entry_element = undefined;
    this._children = [];
};
inherits(AllThreadsTagModerator, TagModerator);

AllThreadsTagModerator.prototype.addChild = function(child) {
    this._children.push(child);
};

AllThreadsTagModerator.prototype.getChildCount = function() {
    return this._children.length;
};

AllThreadsTagModerator.prototype.removeChild = function(child) {
    var idx = $.inArray(child, this._children);
    if (idx == -1) {
        return;
    }
    this._children.splice(idx, 1);
};

AllThreadsTagModerator.prototype.hideButtons = function() {
    this._acceptBtn.hide();
    this._rejectBtn.hide();
};

AllThreadsTagModerator.prototype.setTagEntryElement = function(element) {
    this._tag_entry_element = element;
};

AllThreadsTagModerator.prototype.afterActionHandler = function() {
    var me = this;
    this._tag_entry_element.fadeOut('fast');
    this._element.fadeOut('fast', function() { me.dispose() });
};

AllThreadsTagModerator.prototype.dispose = function() {
    this._tag_entry_element.fadeOut('fast', function() {
        $.each(this._children, function(idx, child) {
            child.dispose();
        });
    });
    AllThreadsTagModerator.superClass_.dispose.call(this);
};

AllThreadsTagModerator.prototype.decorate = function(element) {
    this._element = element;

    //var controls = new TagModerationControls();
    //controls.setParent(this);

    //var tagId = $(element).data('tagId');
    //controls.setTagId(tagId);

    var threads_data = [];
    $(element).find('.thread-info').each(function(idx, element) {
        var id = $(element).data('threadId');
        var title = $(element).data('threadTitle');
        threads_data.push([id, title]);
    });
    var acceptBtn = element.find('button.accept');
    var rejectBtn = element.find('button.reject');
    setupButtonEventHandlers(acceptBtn, this.getHandler('accept'));
    setupButtonEventHandlers(rejectBtn, this.getHandler('reject'));
    this._acceptBtn = acceptBtn;
    this._rejectBtn = rejectBtn;
};

(function() {
    $('.suggested-tag-row').each(function(idx, element) {
        var tagEntry = $(element);
        var tagId = tagEntry.data('tagId');

        var tagMod = new AllThreadsTagModerator();
        tagMod.decorate(tagEntry.next());
        tagMod.setTagId(tagId);
        tagMod.setTagEntryElement(tagEntry);

        tagEntry.find('.thread-info').each(function(idx, element) {
            var threadMod = new PerThreadTagModerator();
            threadMod.setTagId(tagId);
            threadMod.setParent(tagMod);
            tagMod.addChild(threadMod);
            threadMod.decorate($(element));
        });

    });
})();
