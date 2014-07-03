.. _dependencies:

===================
Askbot Dependencies
===================

Askbot depends on quite a few other packages. Normally those dependencies will be
automatically resolved with setuptools (i.e. when you run `easy_install` or `python setup.py install`). 

However, if something does not go well - e.g.
some dependency package site is not accessible, please 
download and install them manually:

* django-1.1.2_
* django-debug-toolbar_
* South_
* recaptcha-client_
* markdown2_
* html5lib_
* python-openid_
* django-keyedcache_
* django-threaded-multihost_
* mysql-python_

If any of the provided links
do not work please try to look up those packages or notify askbot maintainers at admin@askbot.org.

.. _django-1.1.2: http://www.djangoproject.com/download/1.1.2/tarball/
.. _django-debug-toolbar: http://github.com/robhudson/django-debug-toolbar
.. _South: http://www.aeracode.org/releases/south/
.. _recaptcha-client: http://code.google.com/p/django-recaptcha/
.. _markdown2: http://code.google.com/p/python-markdown2/
.. _html5lib: http://code.google.com/p/html5lib/
.. _python-openid: http://github.com/openid/python-openid
.. _django-keyedcache: http://bitbucket.org/bkroeze/django-keyedcache/src
.. _django-threaded-multihost: http://bitbucket.org/bkroeze/django-threaded-multihost/src
.. _mysql-python: http://sourceforge.net/projects/mysql-python/
.. _mod_wsgi: http://code.google.com/p/modwsgi/
