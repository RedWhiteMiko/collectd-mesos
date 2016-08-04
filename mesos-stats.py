#! /usr/bin/python
# Copyright 2015 Ray Rodriguez
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collectd
import collections

import mesos_collectd_stats


IS_MASTER = False
PREFIX = "mesos-slave"
MESOS_CLUSTER = "cluster-0"
MESOS_INSTANCE = "slave-0"
MESOS_PATH = "/usr/sbin"
MESOS_HOST = "localhost"
MESOS_PORT = 5051
MESOS_URL = ""
VERBOSE_LOGGING = False

Stat = collections.namedtuple('Stat', ('type', 'path'))

# DICT: Common Metrics in 0.19.0, 0.20.0, 0.21.0, 0.22.0 and 0.23.0
STATS_MESOS = {
    # Statistics
    "cpus_limit": Stat("gauge", "statistics/cpus_limit"),
    "cpus_system_time_secs": Stat("counter", "statistics/cpus_system_time_secs"),
    "cpus_user_time_secs": Stat("counter", "statistics/cpus_user_time_secs"),
    "mem_anon_bytes": Stat("bytes", "statistics/mem_anon_bytes"),
    "mem_cache_bytes": Stat("bytes", "statistics/mem_cache_bytes"),
    "mem_critical_pressure_counter": Stat("gauge", "statistics/mem_critical_pressure_counter"),
    "mem_file_bytes": Stat("bytes", "statistics/mem_file_bytes"),
    "mem_limit_bytes": Stat("bytes", "statistics/mem_limit_bytes"),
    "mem_low_pressure_counter": Stat("gauge", "statistics/mem_low_pressure_counter"),
    "mem_mapped_file_bytes": Stat("bytes", "statistics/mem_mapped_file_bytes"),
    "mem_medium_pressure_counter": Stat("gauge", "statistics/mem_medium_pressure_counter"),
    "mem_rss_bytes": Stat("bytes", "statistics/mem_rss_bytes"),
    "mem_swap_bytes": Stat("bytes", "statistics/mem_swap_bytes"),
    "mem_total_bytes": Stat("bytes", "statistics/mem_total_bytes"),
    "mem_unevictable_bytes": Stat("bytes", "statistics/mem_unevictable_bytes"),
}

# DICT: Mesos 0.19.0, 0.19.1
STATS_MESOS_019 = {}

# DICT: Mesos 0.20.0, 0.20.1
STATS_MESOS_020 = {}

# DICT: Mesos 0.21.0, 0.21.1
STATS_MESOS_021 = {}

# DICT: Mesos 0.22.0, 0.22.1
STATS_MESOS_022 = {}


def configure_callback(conf):
    mesos_collectd_stats.configure_callback(conf, IS_MASTER, PREFIX, MESOS_CLUSTER,
                                            MESOS_INSTANCE, MESOS_PATH, MESOS_HOST,
                                            MESOS_PORT, MESOS_URL, VERBOSE_LOGGING)


def read_callback():
    mesos_collectd_stats.read_callback(IS_MASTER, STATS_MESOS, STATS_MESOS_019,
                                       STATS_MESOS_020, STATS_MESOS_021,
                                       STATS_MESOS_022)


collectd.register_config(configure_callback)
collectd.register_read(read_callback)
