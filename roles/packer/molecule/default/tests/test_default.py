import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

@pytest.mark.parametrize('pkg', [
    'python3'
])
def test_pkg(host, pkg):
    package = host.package(pkg)
    assert package.is_installed

@pytest.mark.parametrize('file', [
    '/usr/local/bin/packer'
])
def test_bin_file(host, file):
    packer_file = host.file(file)
    assert packer_file.user == "root"
    assert packer_file.group == "root"
    assert packer_file.mode == 0o755
