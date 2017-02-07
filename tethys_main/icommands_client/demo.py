from icommands import ICommands

if __name__ == "__main__":

    IRODS_HOST = 'hydrotest41.renci.org'
    IRODS_PORT = '1247'
    IRODS_DEFAULT_RESOURCE = 'hydrotest41Resc'
    IRODS_ZONE = 'hydrotest41Zone'
    IRODS_USERNAME = 'hsproxy'
    IRODS_AUTH = 'proxywater1'

    icommands = ICommands()

    icommands.set_user_session(username=IRODS_USERNAME, password=IRODS_AUTH, host=IRODS_HOST,
                         port=IRODS_PORT, def_res=IRODS_DEFAULT_RESOURCE, zone=IRODS_ZONE,
                         userid=0, sess_id=None)



    icommands.getFile("/hydrotest41Zone/home/hsproxy/e438bf9871ec402b8f2cf27f37f10081/data/contents/Spot_Bamako_Mali_980mb.tif",
                      "/tmp/Spot_Bamako_Mali_980mb.tif")

    icommands.delete_user_session()