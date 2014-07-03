=======================
Sending email to askbot
=======================

Askbot supports asking questions by email via the IMAP protocol,
answering by email is not yet supported.

.. note::
    This feature is still experimental and some emails will not
    be parsed, please report any issues at the askbot forum.

To enable the feature, please:

* set up an IMAP mailbox called "INBOX"
* in your ``settings.py`` file fill out values
  ``IMAP_HOST``, ``IMAP_HOST_USER``, ``IMAP_HOST_PASSWORD``,
  ``IMAP_PORT`` and ``IMAP_USE_TLS``
* in the site :ref:`live settings <live-settings>`, enable the 
  feature
* set up a cron job to periodically run command
  :ref:`post_emailed_questions <email-related-commands>`.
  This command will connect to the inbox, and post questions,
  based on the incoming messages.

The email address to send the questions will be
``<IMAP_HOST_USER>@<IMAP_HOST>``. Also, there is a quite strict
requirement to the format of incoming messages - described
in a response to any incorrectly formatted emails.

.. warning::
    the "INBOX" used to post messages to askbot must be dedicated
    do not use any other mailbox as all messages
    are **automatically deleted** after each processing.
