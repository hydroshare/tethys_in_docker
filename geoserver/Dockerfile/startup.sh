#!/bin/bash
cd /Dockerfile
python gen_build_time_dynamic_files.py

# Generate the geoserver_startup.sh
python gen_runtime_dynamic_files.py

# Start with supervisor -----------------------------------------------------------------------------------------------#
/usr/bin/supervisord -c $GEOSERVER_HOME/supervisord.conf