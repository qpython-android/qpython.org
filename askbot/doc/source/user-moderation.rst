=========================
User moderation in Askbot
=========================

.. note::

 This is a draft specification

Concepts
=========

**User status**. The following user status levels are meaningful in askbot:

* administrator - user with moderation and administration privileges
* moderator - user with moderation privileges
* approved - user that can make full use of the forum
* watched - like approved user, except his/her contributions are not sent by email
* suspended - only can edit own existing posts and own profile, will see suspension message
* blocked - can't do anything except send feedback, will see blocking message

These status levels are mutually exclusive.

**Admin panel**. Each user has a sub/view of his/her account giving tools.

Admin panel exposes moderation and administration tools. Note that there are some
moderation tools located in other places (e.g. question views).

If a user can see own admin panel, the panel will always be restricted in function, because
it never makes to communicate by email with him/herself, etc.

**Moderation tools**:

* change user status in range from blocked to approved
* arbitrarily add/subtract reputation and leave a message
* send PM to user
* merge tags (tags view, )
* merge questions (need special tool - sticky selection in search?)

**Restrictions on moderators**

* cannot moderate other moderators or admins, cannot access admin tools

**Administration tools**:

* edit user profiles
* change user status to moderators and remove it
* merge users
* delete accounts
* delete user contributions
