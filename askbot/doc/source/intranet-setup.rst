==========================================================
Setting up Askbot for use on the closed network (Intranet)
==========================================================

When using Askbot on the Intranet (for example - within your 
Company network), it will be useful to disable references to
all external resources - such as custom fonts, gravatars.

Please change the following settings in your ``settings.py`` file::

    ASKBOT_USE_LOCAL_FONTS=True

In addition, in the "live settings":
* disable gravatar in "settings->User settings"

If you would like to password/protect your site 
(achievable via "access control settings" -> "allow only registered users..."),
and at the same time be able to have some dedicated service 
to read your site without authentication, add
IP addresses of that service to a tuple ``ASKBOT_INTERNAL_IPS``
in your ``settings.py`` file.
