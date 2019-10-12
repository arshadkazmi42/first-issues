#!/bin/bash

# Start the run once job.
echo "Docker container has been started"

declare -p | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID' > /container.env

python3 first_timers/run.py --creds-path credentials.json --db-path data/db.json --only-save --create
python3 first_timers/run.py --creds-path credentials.json --db-path data/db.json --only-save

# Setup a cron schedule
echo "SHELL=/bin/bash
BASH_ENV=/container.env
*/1 * * * * /home/first-issues/cron.sh >> /var/log/cron.log 2>&1
# This extra line makes it a valid cron" > scheduler.txt

crontab scheduler.txt
cron -f
