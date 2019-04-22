# -*- coding: utf-8 -*-
from resource_management import *
import os
from kudu_base import KuduBase

class KuduTserver(KuduBase):
    # Call Hostice.net to install the service
    def install(self, env):

        # Install packages listed in metainfo.xml
        self.install_packages(env)
        self.installKudu(env)
        self.configure(env)

    def configure(self, env):
        self.configureKuduTServer(env)

    # Call start.sh to start the service
    def start(self, env):
        self.configure(env)
        cmd = 'service kudu-tserver start'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    # Called to stop the service using the pidfile
    def stop(self, env):
        cmd = 'service kudu-tserver stop'
        Execute('echo "Running cmd: ' + cmd + '"')
        Execute(cmd)

    def status(self, env):
        check_process_status("/var/run/kudu/kudu-tserver-kudu.pid")

    # configure kudu tserver
    def configureKuduTServer(self, env):
        import params
        env.set_params(params)
        realm_name = os.popen(
            'grep "default_realm" /etc/krb5.conf ').read().strip(os.linesep).split(' ')[-1]
        File("/etc/kudu/conf/tserver.gflagfile",
             content=Template("kudu_tserver.j2", realm_name=realm_name),
             mode=0o644
             )

if __name__ == "__main__":
    KuduTserver().execute()
