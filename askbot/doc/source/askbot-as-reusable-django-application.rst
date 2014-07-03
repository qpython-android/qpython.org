=====================================
Askbot as reusable django application
=====================================

Askbot can be used both as as dedicated site and as an application
within a larger site. There are still issues to resolve to make askbot
a truly reusable app, but some are already solved.

This page is a guide for using askbot as an independent app and it is 
somewhat technical.

.. _adding-askbot-to-pre-existing-site:
Adding askbot to a pre-existing site
====================================

If you already have a django site with users, after adding askbot
to your project, run a management command just once::

    python manage.py add_missing_subscriptions

.. note::
    This only applies to users registered before the installation of Askbot.
    Newer users will have default subscription records
    created automatically, by the Django's ``post_save`` signal.
    
    The email subscription settings are also created automatically
    when certain pages are visited and when ``send_email_alerts``
    command is run, so it is not mandatory to run
    ``add_missing_subscriptions``.

.. _askbot-with-alternative-login-system:
Using alternative login system
==============================

Askbot has a bundled application for user login and registration,
but it can be replaced with any other.
Just remove ``'askbot.deps.django_authopenid'``
from the ``INSTALLED_APPS``,
remove ``'askbot.deps.django_authopenid.backends.AuthBackend'``
from the ``AUTHENTICATION_BACKENDS``,
install another registration app
and modify ``LOGIN_URL`` and ``LOGOUT_URL`` accordingly.

If you are adding Askbot to a django site that already has
registered users, please see :ref:`this section <adding-askbot-to-pre-existing-site>`.

There are two caveats.

Firstly, if you are using some other login/registration app,
please disable feature
"settings"->"data entry and display"->"allow posting before logging in".

This may be fixed in the future by adding a snippet of code to run
right after the user logs in - please ask at askbot forum if you are 
interested.

Secondly, disable setting "settings"->"user settings"->"allow add and remove login methods".
This one is specific to the builtin login application which allows more than one login
method per user account.
