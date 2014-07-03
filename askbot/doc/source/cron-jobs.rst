==========================================
Automation of maintenance jobs with cron
==========================================

There are routine tasks that should be performed periodically
from the command line. They can be automated via cron_ jobs

File askbot_cron_job_ has a sample script that can be run say hourly

The script currently does two things: (1) sends delayed email alerts and
(2) awards badges. These two actions can be separated into two separate jobs,
if necessary

.. _cron: http://www.unixgeeks.org/security/newbie/unix/cron-1.html
.. _askbot_cron_job: http://github.com/ASKBOT/askbot-devel/blob/master/askbot/cron/askbot_cron_job

