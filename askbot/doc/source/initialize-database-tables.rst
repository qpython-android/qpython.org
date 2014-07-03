.. _initialize-database-tables:

=======================================================
Initialization and upgrade of the database for Askbot
=======================================================

When you install Askbot the first time and any time you upgrade the software, run these two commands::

    python manage.py syncdb

.. versionchanged:: 0.7.21
    When the script asks you if you want to create a superuser, answer yes if you want to create one. By default Askbot sets admin status(superuser) for the first user created automatically but also supports this form.

.. deprecated:: 0.7.21
    When the script asks you if you want to create a superuser, answer **no**.

Then run::

    python manage.py migrate askbot
    python manage.py migrate django_authopenid #embedded login application

.. note::

    When upgrading - do not skip to back up the database before proceeding!!!
    Things can break and it is better to be safe than sorry. Even better -
    do run two installations of your project - one for production deployment
    and the second one - for testing the upgrade. When you are sure that
    your upgrade works, just switch the testing installation for the former production one.

Now run the Django development server and check that everything works::

    python manage.py runserver `hostname -i`:8000 #or use some other port number > 1024

.. note::

    `hostname -i` is a Unix command returning the IP address of your system, you can also type 
    the IP manually or replace it with word `localhost` if you are installing askbot 
    on a local machine.

Connect to the Django development server with your Web browser. The address is the name
(or IP address) of your site followed by ":8000" (or whatever port number you chose above).
Once the fresh copy of Askbot appears in your browser, create a new account at the site.
This will be your administrator account.

.. deprecated:: 0.7.20
   Finally, turn the newly added user into a superuser by running::

       python manage.py add_admin 1

.. versionadded:: 0.7.20
   In the new version of Askbot the first user you create on the site will be added as administrator.

Here number 1 is the numeric id of the first user, enter a different number, if it is indeed different.

Your basic installation is now complete. Many settings can be 
:ref:`changed at runtime <run-time-configuration>` by following url `/settings`.

If you choose to host a real website, please read
section :ref:`deployment`.


