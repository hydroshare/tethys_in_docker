# tethys_in_docker

Experimental

How to use:

####Some usages:
####0) install latest docker-engine and docker-compose on host

####1) build tethys_in_docker in one command:
sudo ./tethys_rebuild release-candidate-140-1

####2) install an app:
cd apps
git clone APP_GIT_URL
./tethys_install_app APP_FOLDER_NAME

####3) uninstall a app:
./tethys_uninstall_app APP_PACKAGE_NAME
