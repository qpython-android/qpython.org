=========
Footnotes
=========

This page summarizes additional information that might be useful
for deployment of development of ``askbot``.

.. _git:

Git
===

At askbot we use ``git`` to keep track of the source code,
and the main repository is hosted at
`github <https://github.com/ASKBOT/askbot-devel>`_.

With git you can always grab 
the latest code of askbot from the 
latest ``askbot`` code::

    git clone git://github.com/ASKBOT/askbot-devel.git

Do some customization by editing files and then::

    git add <list-of-changed-files>
    git commit -m 'explain why you have changed some files'

Bring updates from the main repo::

    git git fetch origin master:github #.. onto a local branch called github
    git checkout master
    git merge github

If all goes well, you are done. Otherwise, you may need to
`resolve the conflict <http://www.kernel.org/pub/software/scm/git/docs/user-manual.html#resolving-a-merge>`_.

Here is a 
`good basic tutorial <http://www.ralfebert.de/tutorials/git/>`_
about git,
more comprehensive ones
`here <http://book.git-scm.com/>`_ 
and 
`there <http://help.github.com/>`_.
Finally, you also may want to visit the 
official git `reference <http://gitref.org>`_
and `documentation <http://www.kernel.org/pub/software/scm/git/docs/>`_.
There are `screencasts <http://gitcasts.com/>`_ too.

.. _pip:

Pip
===

``Pip`` is the best package management tool for python, allows to install and
unistall python packages, supports installation from source code repositories 
and much more.

For more information about ``pip``,
including its installation, 
please visit the `pip package page <http://pypi.python.org/pypi/pip>`_
and the links within.

.. _pip-pypi: http://pypi.python.org/pypi/pip
.. _git-csm-book: http://book.git-scm.com/
.. _git-basic-tutorial: http://www.ralfebert.de/tutorials/git/
.. _git-github-tutorial: http://help.github.com/
.. _git-docs: http://www.kernel.org/pub/software/scm/git/docs/
.. _git-reference:  http://gitref.org
.. _git-casts: http://gitcasts.com/
.. _git-resolve-conflict: http://www.kernel.org/pub/software/scm/git/docs/user-manual.html#resolving-a-merge
