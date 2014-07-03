.. _debugging:

================================================
Debugging Askbot (and other Django applications)
================================================

This document describes techniques that can be used to debug Askbot and other Django projects
If you discover new debugging techniques, please add here.

.. _runserver:
Use development server for debugging
------------------------------------

Django comes with a handy development webserver that can be started with the command::

    python manage.py runserver

With the combination of runserver,
the :ref:`python debugger <pdb>`,
and even inserted "print" statements directly in the code
it is possible to "look into" the program as it runs.

Inspect the log file
--------------------

By default askbot will log errors into file `log/askbot.log` within the
project directory. See what's inside that file.

Note that in the production setups there are many log files - for the
production webserver, database, etc.

.. _pdb:
Use Python debugger
-------------------

In the problematic portion of the code, insert lines::

    import pdb
    pdb.set_trace()

Then fire up the :ref:`runserver <runserver>` and step through the program.
When you see prompt starting with `(pdb)`
type `help` and see what options there are.

Use logging in code
---------------------

Please remember that log files may contain plaintext passwords, etc.

Please do not add print statements - at least do not commit them to git
because in some environments printing to stdout causes errors

Instead use python logging this way::

    #somewere on top of file
    import logging

    #anywhere below
    logging.debug('this maybe works')
    logging.error('have big error!')
    #or even
    logging.debug('') #this will add time, line number, function and file record 
    #sometimes useful record for call tracing on its own
    #etc - take a look at http://docs.python.org/library/logging.html

in Askbot logging is currently set up in settings.py
please update it if you need - in older revs logging strings have less info

messages of interest can be grepped out of the log file by module/file/function name
e.g. to take out all django_authopenid logs run::

    >grep 'askbot\/django_authopenid' log/django.askbot.log | sed 's/^.*MSG: //'

in the example above `sed` call truncates out a long prefix
and makes output look more meaningful

Using django debug toolbar
---------------------------

Askbot works with django debug toolbar that displays a lot of useful diagnostics about
your site.

To enable the toolbar set parameter `DEBUG = True` in the `settings.py` file. Also you will
need to add your IP address to the tuple `INTERNAL_IPS` in the same `settings.py` file.

If your debugging site runs under apache server, check 
that debug toolbar media is loaded correctly through an `alias` configuration directive in 
the appropriate place of your apache configuration file.
