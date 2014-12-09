#!/bin/bash
./manage.py collectstatic --noinput && sudo /etc/init.d/apache2 reload
