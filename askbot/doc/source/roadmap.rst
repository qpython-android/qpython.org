Intro
=========
ROADMAP aims to streamline activities of the Askbot open source project and
to minimize ad-hoc approaches of "big-picture" level.

Askbot is a Question and Answer system for the normal people!

Basic principles of the project
==================================

We favor plain and minimalistic style of programming, but pay
  attention to detail - especially details of user experience.

We try do develop using the following workflow:

* specify problem that we try to solve
* create requirements that will guarantee a solution, once met
* dream up some implementation ideas (maybe even some sketches on the paper)
* discuss and decide on the best one
* write and test code

The process doesn't have to be this formal all the time, but trying to stick
to some subset of this almost always helps! 
Especially it helps to iron out disagreements between
individual programmers (which if you are one - you know are qute common).

Ad-hoc programming - i.e. simply go and add code - is not really encouraged.
This works fine in the one person team or when the team consists of 
best friends, but is almost sure to fail in a heterogenous group.

Architecture and Requirements
=====================================
Obviously Django and Python are pre-made choices - so this
is not going to change any time soon. At this point all of
the client side Javascript is written using jQuery library.

Our basic principle is that Askbot should be a mashable Q&A component.
Askbot is an application written in Python/Django. So it should be 
distributable as a Django App alone, but can be deployed as a dedicated site
with the script "askbot-setup", that also ships with askbot.

If we develop a sub-system that can be used in the broader scope - 
we package it as a separate django application (login system is one example).

We will start using Google Closure library soon!

Skins
-----------
Skins eventually must be upgrade-stable - that is people who created custom
skins should not need to change anything if something changes in the code

Admin interface
-----------------------
We use a forked application "livesettings" that ideally should be merged
back to the original livesettings application.
