import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sensu_backend_config(host):
    config = host.run("sudo systemctl status sensu-backend")
    assert config.rc == 0
