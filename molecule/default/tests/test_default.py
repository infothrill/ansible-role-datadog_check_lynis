# -*- coding: utf-8 -*-
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nsd_check_deployed(host):
    datadog_dir = "/etc/datadog-agent"  # agent 6+
    assert host.file(os.path.join(datadog_dir, "checks.d/lynis.py")).exists
