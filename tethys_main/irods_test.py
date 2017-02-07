import shutil
import time
import logging
import os

from irods.session import iRODSSession
from irods.models import Collection, DataObject
from irods.column import Criterion

logger = logging.getLogger(__name__)


def download_res_bag_via_icommands(res_id,
                                  host,
                                  port,
                                  user,
                                  password,
                                  zone,
                                  irods_base_collection_path,
                                  local_save_to_path,
                                  remove_old=True):
    try:

        download_list = []
        if irods_base_collection_path[-1] != "/":
            irods_base_collection_path += "/"
        if local_save_to_path[-1] != "/":
            local_save_to_path += "/"

        sess = iRODSSession(host=host, port=port, user=user, password=password, zone=zone)

        # query res files in this resources
        query_results = sess.query(DataObject.name, Collection.name).\
            filter(Criterion('like', Collection.name, "%{0}{1}%".format(irods_base_collection_path, res_id))).all()

        start_time_all = time.time()

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

            irod_data_obj = sess.data_objects.get(irods_res_file_path)

            start_time_onefile = time.time()
            with irod_data_obj.open("r") as file_obj_src:
                with open(local_res_file_path, 'wb') as file_obj_target:
                    # see: http://blogs.blumetech.com/blumetechs-tech-blog/2011/05/faster-python-file-copy.html
                    shutil.copyfileobj(file_obj_src, file_obj_target, 10*1024*1024)  # 10mb buffer
            end_time_onefile = time.time()

            msg = "Done in {0} sec, {1} sec Elapsed".format((end_time_onefile-start_time_onefile),
                                                            (end_time_onefile-start_time_all))
            print(msg)
            logger.debug(msg)
            download_list.append(local_res_file_path)

        msg = "All Done in {0} sec".format(time.time()-start_time_all)
        print(msg)
        logger.debug(msg)

    except Exception as ex:

        print(ex.message)
        logger.exception(ex.message)

    finally:
        return download_list


if __name__ == "__main__":

    res_id = "6c1422bf5516459b9e0359ac954bd891"
    host = "hydrotest41.renci.org"
    port = 1247
    user = 'hsproxy'
    password = 'proxywater1'
    zone = 'hydrotest41Zone'

    irods_base_collection_path = "/hydrotest41Zone/home/hsproxy/"
    local_save_to_path = '/tmp/'

    download_list = download_res_bag_via_icommands(res_id,
                                                  host,
                                                  port,
                                                  user,
                                                  password,
                                                  zone,
                                                  irods_base_collection_path,
                                                  local_save_to_path)
    print download_list
