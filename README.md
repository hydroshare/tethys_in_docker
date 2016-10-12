# tethys_in_docker

Experimental

####Some usages:

####0) install latest docker-engine and docker-compose on host

For Ubuntu, see https://docs.docker.com/engine/installation/linux/ubuntulinux/

and https://docs.docker.com/engine/installation/linux/ubuntulinux/

git clone this repo

####1) build tethys_in_docker in one command:

sudo ./tethys_rebuild release-candidate-140-1

####2) install an app:

cd apps

git clone APP_GIT_URL

./tethys_install_app APP_FOLDER_NAME

####3) uninstall a app:

./tethys_uninstall_app APP_PACKAGE_NAME


####4) create a new app (using tethys scaffold)

./tethys_create_app APP_NAME