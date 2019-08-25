import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sensu_backend_config(host):
    config = host.run("sudo systemctl status sensu-backend")
    assert config.rc == 0

def test_sensu_backend_local_port(host):
    local_port = host.socket("tcp://127.0.0.1:3000")
    assert local_port.is_listening


def test_sensu_backend_and_sensu_agent_running_and_enabled(host):
    sensu_backend_service = host.service("sensu-backend")
    assert sensu_backend_service.is_running
    assert sensu_backend_service.is_enabled

    sensu_agent_service = host.service("sensu-agent")
    assert sensu_agent_service.is_running
    assert sensu_agent_service.is_enabled
