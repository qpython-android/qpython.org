/**
 * askbot_imageuploader.js
 *
 * Copyright 2012, Askbot SpA
 * Released under License.
 *
 * License: http://tinymce.moxiecode.com/license
 * Contributing: http://tinymce.moxiecode.com/contributing
 */

(function() {
    var insertIntoDom = function(url, description) {
        var content = '<img src="' + url;
        if (description) {
            content = content + '" alt="' + description;
        }
        content = content + '"/>';

        tinyMCE.activeEditor.focus();
        if (document.selection) {
            //this branch is a work around the IE "this" quirk
            var sel = document.selection.createRange(); 
            sel.pasteHTML(content);
        } else {       
            var sel = tinyMCE.activeEditor.selection;
            sel.setContent(content);
        }
    };

    var modalMenuHeadline = gettext('Upload an image');

    var createDialog = function() {
        var dialog = new FileUploadDialog();
        dialog.setHeadingText(modalMenuHeadline);
        dialog.setPostUploadHandler(insertIntoDom);
        dialog.setUrlInputTooltip('Or paste image url here');
        dialog.setInputId('askbot_imageuploader_input');
        $(document).append(dialog.getElement());
        return dialog;
    };

    var dialog = undefined;

    var getDialog = function() {
        if (dialog === undefined) {
            dialog = createDialog();
        }
        return dialog;
    };

	// Load plugin specific language pack
	tinymce.PluginManager.requireLangPack('askbot_imageuploader');

	tinymce.create('tinymce.plugins.AskbotImageUploaderPlugin', {
		/**
		 * Initializes the plugin, this will be executed after the plugin has been created.
		 * This call is done before the editor instance has finished it's initialization so use the onInit event
		 * of the editor instance to intercept that event.
		 *
		 * @param {tinymce.Editor} ed Editor instance that the plugin is initialized in.
		 * @param {string} url Absolute URL to where the plugin is located.
		 */
		init : function(ed, url) {
			// Register the command so that it can be invoked by using tinyMCE.activeEditor.execCommand('mceAskbotImageUploader');
			ed.addCommand('mceAskbotImageUploader', function() {
                //start file uploader modal menu
                var dialog = getDialog();
                dialog.show();
            });

			// Register askbot_imageuploader button
			ed.addButton('askbot_imageuploader', {
				title : gettext('Insert image'),
				cmd : 'mceAskbotImageUploader'
				//image : url + '/img/askbot_leuploader.gif'
			});

			// Add a node change handler, selects the button in the UI when a image is selected
			ed.onNodeChange.add(function(ed, cm, n) {
				cm.setActive('askbot_imageuploader', n.nodeName == 'IMG');
			});
		},

		/**
		 * Creates control instances based in the incomming name. This method is normally not
		 * needed since the addButton method of the tinymce.Editor class is a more easy way of adding buttons
		 * but you sometimes need to create more complex controls like listboxes, split buttons etc then this
		 * method can be used to create those.
		 *
		 * @param {String} n Name of the control to create.
		 * @param {tinymce.ControlManager} cm Control manager to use inorder to create new control.
		 * @return {tinymce.ui.Control} New control instance or null if no control was created.
		 */
		createControl : function(n, cm) {
			return null;
		},

		/**
		 * Returns information about the plugin as a name/value array.
		 * The current keys are longname, author, authorurl, infourl and version.
		 *
		 * @return {Object} Name/value array containing information about the plugin.
		 */
		getInfo : function() {
			return {
				longname : 'AskbotImageUploader plugin',
				author : 'Askbot SpA, Chile',
				authorurl : 'http://askbot.com',
				infourl : 'http://github.com/ASKBOT/askbot-devel/',
				version : '0.1'
			};
		}
	});

	// Register plugin
	tinymce.PluginManager.add('askbot_imageuploader', tinymce.plugins.AskbotImageUploaderPlugin);
})();
