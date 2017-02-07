from uuid import uuid4
import session
from session import Session, SessionException, IRodsEnv


class ICommands():

    def __init__(self, option=None):
        pass

    def set_user_session(self, username=None, password=None, host=None,
                         port=None, def_res=None, zone=None,
                         userid=0, sess_id=None):
        homedir = "/" + zone + "/home/" + username
        userEnv = IRodsEnv(
            pk=userid,
            host=host,
            port=port,
            def_res=def_res,
            home_coll=homedir,
            cwd=homedir,
            username=username,
            zone=zone,
            auth=password,
            irods_default_hash_scheme='MD5'
        )
        if sess_id is None:
            self.session = Session(session_id=uuid4())
            self.environment = self.session.create_environment(myEnv=userEnv)
        else:
            self.session = Session(session_id=sess_id)
            if self.session.session_file_exists():
                self.environment = userEnv
            else:
                self.environment = self.session.create_environment(myEnv=userEnv)

        self.session.run('iinit', None, self.environment.auth)
        session.ACTIVE_SESSION = self.session


    def delete_user_session(self):
        if  self.session.session_file_exists():
            self.session.delete_environment()


    def getFile(self, src_name, dest_name):
        self.session.run("iget", None, '-f', src_name, dest_name)



    def exists(self, name):
        try:
            stdout = self.session.run("ils", None, name)[0]
            return stdout != ""
        except SessionException:
            return False

    def listdir(self, path):
        stdout = self.session.run("ils", None, path)[0].split("\n")
        listing = ([], [])
        directory = stdout[0][0:-1]
        directory_prefix = "  C- " + directory + "/"
        for i in range(1, len(stdout)):
            if stdout[i][:len(directory_prefix)] == directory_prefix:
                dirname = stdout[i][len(directory_prefix):].strip()
                if dirname:
                    listing[0].append(dirname)
            else:
                filename = stdout[i].strip()
                if filename:
                    listing[1].append(filename)
        return listing

    def size(self, name):
        stdout = self.session.run("ils", None, "-l", name)[0].split()
        return int(stdout[3])
