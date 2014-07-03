.. _enable_mathjax:

==========================
Enabling MathJax in Askbot
==========================

MathJax_ is a rendering engine for mathematical
expressions (based on cross-browser javascript code). On a MathJax-enabled site, such as Askbot you can display
perfectly formatted mathematical formulae.

However, MathJax distribution is very large and is not shipped with Askbot.

To enable MathJax on your site, please do the following:

Decide where you want to store mathjax (e.g. to share it with other applications as well)::

   cd /some/directory

Follow `mathjax installation instructions`_

Edit webserver configuration so that url `http://example.com/mathjax`
points to that directory and file `MathJax.js` is available at 
`http://example.com/mathjax/MathJax.js`. 
  
For Apache, a following line in the configuration file (maybe within a VirtualHost section) will do::

    Alias /mathjax/ /filesystem/path/to/mathjax/

Finally, enable MathJax in Askbot: "settings" -> "Markup formatting", check "Enable MathJax" and
enter url `http://example.com/mathjax` (link "settings" is available to site administrators in the upper right corner of the forum pages).

.. note::

    your actual forum site must be served from the **same domain and subdomain**
    as mathjax. This is **very important** for Firefox and some other browsers adhering
    to the `same origin policy`_ for the browser cookies. Mathjax does use cookies to 
    store math display settings.

One day enabling MathJax will be even easier, but `some more work`_ needs to be done for this to happen.

.. _MathJax: http://www.mathjax.org/
.. _`some more work`: http://bugs.askbot.org/issues/27
.. _`mathjax installation instructions`: http://www.mathjax.org/resources/docs/?installation.html
.. _`same origin policy`: http://en.wikipedia.org/wiki/Same_origin_policy
