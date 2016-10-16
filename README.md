# tethys_in_docker

Experimental

####Some usages:

####0) install latest docker-engine and docker-compose on host

For Ubuntu, see https://docs.docker.com/engine/installation/linux/ubuntulinux/

and https://docs.docker.com/engine/installation/linux/ubuntulinux/

git clone this repo

####1) build tethys_in_docker in one command:

Note: this script will remove existing tethys_main, postgis and ngnix containers, so DB will be gone, apps need to re-install

./tethys_rebuild release-candidate-140-1

####2) install an app:

download the app source if it is not in "apps" folder yet

  cd apps

  git clone APP_GIT_URL

./tethys_install_app APP_FOLDER_NAME (install a specific app)

./tethys_install_app (install all apps in folder 'apps')

./tethys_restart

####3) uninstall an existing app:

./tethys_uninstall_app APP_PACKAGE_NAME

./tethys_restart

####4) create a new app (using tethys scaffold)

./tethys_create_app NEW_APP_NAME
