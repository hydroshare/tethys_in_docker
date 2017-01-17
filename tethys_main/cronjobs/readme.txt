This folder contains cron jobs you want to run in tethys_in_docker_main container

An example:
* * * * * tethys-user /usr/bin/python /apps/datarodsexplorer/tethysapp/data_rods_explorer/enddate_bounds.py
# Do Not Remove This Line

Notes:

1) Syntax
# Minute   Hour   Day of Month       Month          Day of Week       User              Command
# (0-59)  (0-23)     (1-31)    (1-12 or Jan-Dec)  (0-6 or Sun-Sat)
    0        2          12             *                *             User to run as    Command to run with

So "* * * * *" in above example means to run this job every 1 minute

2) A new line must exist at the end of job file, see "# Do Not Remove This Line"

3) Manually copy job files to /etc/cron.d/

4) Manually change file ownership to root:root with permission 644

5) Based on test, docker-compose cannot easily meet (3) and (4), so do it manually in the container