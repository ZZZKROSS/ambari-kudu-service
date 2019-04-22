# -*- coding: utf-8 -*-
from resource_management import *
import os
from kudu_base import KuduBase

class KuduMaster(KuduBase):
    # Call Hostice.net to install the service
    def install(self, env):

        # Install packages listed in metainfo.xml
        self.install_packages(env)
        self.installKudu(env)
        self.configure(env)

    def configure(self, env):
        self.configureKuduMaster(env)

    # Call start.sh to start the service
    def start(self, env):
        self.configure(env)
        cmd = 'service kudu-master start'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    # Called to stop the service using the pidfile
    def stop(self, env):
        cmd = 'service kudu-master stop'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    # Called to get status of the service using the pidfile
    def status(self, env):
        check_process_status("/var/run/kudu/kudu-master-kudu.pid")

    def configureKuduMaster(self, env):
        import params
        env.set_params(params)
        realm_name = os.popen(
            'grep "default_realm" /etc/krb5.conf ').read().strip(os.linesep).split(' ')[-1]
        File("/etc/kudu/conf/master.gflagfile",
             content=Template("kudu_master.j2", realm_name=realm_name),
             mode=0o644
             )

if __name__ == "__main__":
    KuduMaster().execute()
