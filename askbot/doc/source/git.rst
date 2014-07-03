.. _upgrading-with-git:

===============================================
Upgrading Askbot (and other software) with git
===============================================

Git makes it easy to upgrade software, especially if your version is customized.

Upgrading with git consists of three steps:

#. preparing your local repository for the merge
#. bringing the latest version of the code onto your system
#. merging the latest code with your work

Preparing the local repository for merge
-----------------------------------------

Before you can merge the new code, your local repository must be "clean" - that is any changes in the working copy - most likely the local directory must be committed to your local repository.

First, see which branch is currently in the working copy and what is its state::

    > git status

If the output says that the branch is clean, then skip the section below.

Commit any modified files to the local repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the local branch does have modifed files, 
any of those files (or even entire directories) must be added to the repository index with command `git add`::

   > git add <filename>
   > git add <dirname>

If there are several modified files in the same directory, then adding directory will be more convinient.

In Git system index_ is only a part of the repository - it's a record of "scheduled" changes that must be applied in a single batch called "commit_"

After all changed files are added to the index, the index must be committed (really added, if you will) to the repository::

   > git commit -m 'some descriptive message'

Jump into the branch that you want to upgrade
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If it is the current branch that you want to upgrade, then you are ready for the next step, otherwise switch the branch in the working copy with `git checkout`_ command.

Before checking out a branch see what branches are locally available and which one is the current::

    > git branch

Current branch will be marked with an asterisk.

(Note that adding extra arguments the `git branch`_ command will significantly modify its meaning, for example it can create or delete branches)

Now check out the branch you want to merge the new code into::

    > git checkout <branchname>

(Example below assumes that branchname is 'master').

Bring the latest code into your repository
-------------------------------------------

Now to bring in the fresh code from some public repository (for example public "master" branch hosted on github_), run::

   > git fetch origin master:master-github

In the command above (`git fetch`_), `origin` is the name of the repository (also called "remote" repository). By default `origin` repository is the one that you have used to originally clone_ into your system.

The last part of the command `master:master-github` tells that you want to take stuff from branch `master` on the `origin` repository and put it into branch `master-github` on your local repository.

Merge the upgrade into your local repository
-------------------------------------------------

To merge content of one branch into another, run `git merge`_ command::

    > git merge github-master
    Auto-merging askbot/models/__init__.py
    CONFLICT (content): Merge conflict in askbot/models/__init__.py
    Removing askbot/utils/time.py
    Auto-merging askbot/views/readers.py
    Automatic merge failed; fix conflicts and then commit the result.

The command `git merge github-master` means that you indended to merge content
of your local branch `github-master` into the currently checked out branch.

Often, merge will go smoothly, but if you and someone else have edited the same file approximately on the same place, automatic merge will not work on that file. For example the output above tells that there was a "conflict" in file `askbot/models/__init__.py`.

At any time, e.g. during resolving conflicts you can always check which files still have them with `git status` command::

    > git status
    askbot/models/__init__.py: needs merge
    # On branch master
    # Your branch is ahead of 'origin/master' by 91 commits.
    #
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #   new file:   askbot/bin/show_profile_stats.py
    #   modified:   askbot/doc/source/index.rst
    #   new file:   askbot/locale/fi/LC_MESSAGES/django.mo
    #   modified:   askbot/locale/fi/LC_MESSAGES/django.po
    #   new file:   askbot/migrations/0016_auto__del_validationhash.py
    #   modified:   askbot/models/question.py
    #   modified:   askbot/models/user.py
    #   modified:   askbot/skins/default/media/js/com.cnprog.i18n.js
    #   modified:   askbot/skins/default/media/js/org.askbot.output-words.js
    #   modified:   askbot/skins/default/templates/email_base.html
    #   modified:   askbot/skins/default/templates/question.html
    #   modified:   askbot/skins/default/templates/question_list.html
    #   modified:   askbot/skins/default/templates/user_edit.html
    #   modified:   askbot/utils/decorators.py
    #   deleted:    askbot/utils/time.py
    #   modified:   askbot/views/readers.py
    #
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #   unmerged:   askbot/models/__init__.py

If you have merge conflicts - resolve them and commit them into the repository.

To resolve conflicts, open the file in question and find lines that start with `<<<`. Conflict areas are demarcated by `<<<`, `====` and `>>>` patterns.

`====` divides the conflicting versions.

When resolving merge conflicts your options are: accept one of the versions or come up with some compromize.

Decide what is the best course of action, fix the code, remove the conflict demarcation lines and add file to the index with `git add`_::

    > git add askbot/models/__init__.py

At this point it is best not to use wholsale add via a directory (like `git add askbot`)  - because you don't want to accidentally add other conflicting files into the index.

Once all conflicts are resolved, run the `git commit`_ command::

    > git commit -m 'merged with the public master branch'

.. _index: http://book.git-scm.com/1_the_git_index.html
.. _`git commit`: http://www.kernel.org/pub/software/scm/git/docs/git-commit.html
.. _commit: http://www.kernel.org/pub/software/scm/git/docs/git-commit.html
.. _`git checkout`: http://www.kernel.org/pub/software/scm/git/docs/git-checkout.html 
.. _`git branch`: http://www.kernel.org/pub/software/scm/git/docs/git-branch.html 
.. _`git fetch`: http://www.kernel.org/pub/software/scm/git/docs/git-fetch.html 
.. _`git merge`: http://www.kernel.org/pub/software/scm/git/docs/git-merge.html 
.. _`git add`: http://www.kernel.org/pub/software/scm/git/docs/git-add.html 
.. _clone: http://www.kernel.org/pub/software/scm/git/docs/git-clone.html 
.. _github: http://github.com/ASKBOT/askbot-devel
