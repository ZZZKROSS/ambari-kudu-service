#!/usr/bin/env python
from resource_management import *
from resource_management.libraries.script.script import Script
import os, socket

script_dir = os.path.dirname(os.path.realpath(__file__))
files_dir = os.path.join(os.path.dirname(script_dir), 'files')

# server configurations
config = Script.get_config()
tmp_dir = Script.get_tmp_dir()
# hdp_root = config['configurations']['impala-env']['hdp_root']
stack_name = default("/hostLevelParams/stack_name", None)
# hdp_version_buildnum =  config['configurations']['impala-env']['hdp_version_buildnum']

# master params
master_fs_data_dir = config['configurations']['kudu-env']['master_fs_data_dir']
master_fs_wal_dir = config['configurations']['kudu-env']['master_fs_wal_dir']
tserver_fs_data_dir = config['configurations']['kudu-env']['tserver_fs_data_dir']
tserver_fs_wal_dir = config['configurations']['kudu-env']['tserver_fs_wal_dir']
tserver_webserver_port = config['configurations']['kudu-env']['tserver_webserver_port']
master_addrs = config['configurations']['kudu-env']['master_addrs']
master_block_cache_capacity = config['configurations']['kudu-env']['master_block_cache_capacity']
log_force_fsync = config['configurations']['kudu-env']['log_force_fsync']
master_webserver_port = config['configurations']['kudu-env']['master_webserver_port']
master_maintenance_manager_threads = config['configurations']['kudu-env']['master_maintenance_manager_threads']
master_memory_limit_hard_bytes = config['configurations']['kudu-env']['master_memory_limit_hard_bytes']
master_max_log_size = config['configurations']['kudu-env']['master_max_log_size']
default_num_replicas = config['configurations']['kudu-env']['default_num_replicas']
master_ts_rpc_timeout_ms = config['configurations']['kudu-env']['master_ts_rpc_timeout_ms']
max_create_tablets_per_ts = config['configurations']['kudu-env']['max_create_tablets_per_ts']
rpc_max_message_size = config['configurations']['kudu-env']['rpc_max_message_size']

# tserver params
tserver_block_cache_capacity = config['configurations']['kudu-env']['tserver_block_cache_capacity']
tserver_maintenance_manager_threads = config['configurations']['kudu-env']['tserver_maintenance_manager_threads']
tserver_memory_limit_hard_bytes = config['configurations']['kudu-env']['tserver_memory_limit_hard_bytes']
master_rpc_keepalive_time = config['configurations']['kudu-env']['master_rpc_keepalive_time']
tserver_rpc_service_threads = config['configurations']['kudu-env']['tserver_rpc_service_threads']
tserver_rpc_service_queue_length = config['configurations']['kudu-env']['tserver_rpc_service_queue_length']
tserver_reactor_threads = config['configurations']['kudu-env']['tserver_reactor_threads']
tserver_heartbeat_rpc_timeout = config['configurations']['kudu-env']['tserver_heartbeat_rpc_timeout']
current_host_name = socket.gethostname()
hdfs_host = default("/clusterHostInfo/namenode_hosts", [''])[0]
