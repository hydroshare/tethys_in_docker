# tethys_in_docker

Experimental


####0) install latest docker-engine and docker-compose on host

For Ubuntu, see https://docs.docker.com/engine/installation/linux/ubuntulinux/

and https://docs.docker.com/engine/installation/linux/ubuntulinux/

git clone this repo

####1) change/review settings at ./config/config.yaml:

TETHYS_NGINX_DOMAIN_NAME:  (e.g. www.my-tethys-portal.com)

####2) build tethys_in_docker in one command:
./tethys_build

####3) install an app:

download the app source if it is not in "apps" folder yet

  cd apps

  git clone APP_GIT_URL

./tethys_install_app APP_FOLDER_NAME (install a specific app)

./tethys_install_app (install all apps in folder 'apps')


####4) uninstall an existing app:

./tethys_uninstall_app APP_PACKAGE_NAME

./tethys_restart

####5) create a new app (using tethys scaffold)

./tethys_create_app NEW_APP_NAME
