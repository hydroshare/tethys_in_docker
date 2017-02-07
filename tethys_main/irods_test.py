import shutil
import time
import logging
import os

from irods.session import iRODSSession
from irods.models import Collection, DataObject
from irods.column import Criterion
from icommands_client.icommands import ICommands
from hs_restclient import HydroShare, HydroShareAuthBasic

logger = logging.getLogger(__name__)


def download_res_bag_via_icommands(host=None,
                                   port=None,
                                   user=None,
                                   password=None,
                                   zone=None,
                                   default_res=None,
                                   irods_base_collection_path=None,
                                   local_save_to_path=None,
                                   res_id_list=[],
                                   remove_old=True):
    try:

        download_list = []

        start_time_all = time.time()

        icommands = ICommands()
        icommands.set_user_session(username=user, password=password, host=host,
                                   port=port, def_res=default_res, zone=zone,
                                   userid=0, sess_id=None)

        if irods_base_collection_path[-1] != "/":
            irods_base_collection_path += "/"
        if local_save_to_path[-1] != "/":
            local_save_to_path += "/"

        sess = iRODSSession(host=host, port=port, user=user, password=password, zone=zone)
        # loop through all res
        for res_id in res_id_list:

            # query res content files in this resources
            query_results = sess.query(DataObject.name, Collection.name).\
                filter(Criterion('like', Collection.name, "%{0}{1}/data/contents%".format(irods_base_collection_path, res_id))).all()


            irods_res_bag_path = irods_base_collection_path + str(res_id)
            local_res_bag_path = local_save_to_path + str(res_id)

            msg = "Start to download resource {0} to {1}".format(res_id, local_res_bag_path)
            print(msg)
            logger.debug(msg)

            if remove_old and os.path.exists(local_res_bag_path):
                msg = "Removing existing res bag folder: {0}".format(local_res_bag_path)
                print(msg)
                logger.debug(msg)
                shutil.rmtree(local_res_bag_path)

            # print res bag content list
            print query_results
            logger.debug(query_results)

            # loop through all files in this res bag
            for row in query_results.rows:
                res_filename = None
                irods_collection_path = None
                for item in row:
                    if "DATA_NAME" in item.icat_key:
                        res_filename = row[item]
                    elif "COLL_NAME" in item.icat_key:
                        irods_collection_path = row[item]
                    else:
                        raise

                msg = "Downloading {0} from {1}".format(res_filename, irods_collection_path)
                print msg
                logger.debug(msg)

                # create local subfolder if needed
                new_local_res_subfolder_name = irods_collection_path.split(irods_res_bag_path)[1]

                new_local_rse_subfolder_path = local_res_bag_path + new_local_res_subfolder_name
                if not os.path.exists(new_local_rse_subfolder_path):
                    os.makedirs(new_local_rse_subfolder_path)
                local_res_file_path = new_local_rse_subfolder_path + "/" + res_filename

                irods_res_file_path = irods_collection_path + "/" +res_filename

                start_time_onefile = time.time()
                # irods_python_client is not using icommands underneath
                # so it is slow in data tranfer

                # irod_data_obj = sess.data_objects.get(irods_res_file_path)
                # with irod_data_obj.open("r") as file_obj_src:
                #     with open(local_res_file_path, 'wb') as file_obj_target:
                #         # see: http://blogs.blumetech.com/blumetechs-tech-blog/2011/05/faster-python-file-copy.html
                #         shutil.copyfileobj(file_obj_src, file_obj_target, 10*1024*1024)  # 10mb buffer

                # use icommands to do data transfer
                icommands.getFile(irods_res_file_path, local_res_file_path)
                end_time_onefile = time.time()

                msg = "Done in {0} sec, {1} sec Elapsed".format((end_time_onefile-start_time_onefile),
                                                                (end_time_onefile-start_time_all))
                print(msg)
                logger.debug(msg)
                download_list.append(local_res_file_path)

        time_elapesed = time.time()-start_time_all
        msg = "All Done in {0} sec".format(time_elapesed)
        print(msg)
        logger.debug(msg)

        icommands.delete_user_session()

        return download_list, time_elapesed

    except Exception as ex:

        print(ex.message)
        logger.exception(ex.message)




def download_res_bag_via_rest_api(username, password, res_id_list=[]):

    try:
        start_time_all = time.time()
        auth = HydroShareAuthBasic(username=username, password=password)
        hs = HydroShare(auth=auth)

        for res_id in res_id_list:
            print "REST Downloading {0}".format(res_id)
            hs.getResource(res_id, destination='/tmp', unzip=True)

        time_elapesed = time.time() - start_time_all
        print "REST Done in {0}".format(time_elapesed)

        return time_elapesed
    except Exception as ex:
        print ex.message


if __name__ == "__main__":

    res_id_list = [
                    "211fae34ae7b4d51a9b441fcdd1405ac",
                   # "a94af692e2d1442cad3797d23ed7cdf8",
                   #"e438bf9871ec402b8f2cf27f37f10081",
                   #"95d0f197254f4a35a5d5aeb5b1838eb4"  # multiple folders
                   ]

    host = "hydrotest41.renci.org"
    port = 1247
    user = 'hsproxy'
    password = 'proxywater1'
    zone = 'hydrotest41Zone'
    default_res = "hydrotest41Resc"

    irods_base_collection_path = "/hydrotest41Zone/home/hsproxy/"
    local_save_to_path = '/tmp/irods/'
    result_dict = {}
    result_dict["icommands"] = []
    result_dict["rest"]=[]

    rest_username = ""
    rest_password = ""

    run_rounds = 1

    for i in range(run_rounds):
        download_list, time_elapesed = download_res_bag_via_icommands(host=host,
                                                      port=port,
                                                      user=user,
                                                      password=password,
                                                      zone=zone,
                                                      default_res=default_res,
                                                      irods_base_collection_path=irods_base_collection_path,
                                                      local_save_to_path=local_save_to_path,
                                                      res_id_list=res_id_list)

        result_dict["icommands"].append(time_elapesed)

        time_elapesed_rest = download_res_bag_via_rest_api(username=rest_username,
                                                           password=rest_password,
                                                           res_id_list=res_id_list)
        result_dict["rest"].append(time_elapesed_rest)


    print sum(result_dict["icommands"])/len(result_dict["icommands"]), \
          sum(result_dict["rest"])/len(result_dict["rest"])
