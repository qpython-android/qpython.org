#!/bin/sh
#kill -TERM `cat /data/pipaldata/qpythoncommunity_uwsgi.pid`
killall uwsgi
uwsgi -i uwsgi.ini
