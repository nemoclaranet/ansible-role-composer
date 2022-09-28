#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")

def test_shell(host):
    command = host.run("sh --version")
    assert command.rc == 0

composer_bin_file = "/usr/local/bin/composer.phar"
composer_link_to_bin_file = "/usr/local/bin/composer"

def test_motd_file(host):
    file = host.file(composer_link_to_bin_file)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o755

def test_motd_file(host):
    file = host.file(composer_bin_file)
    assert file.exists
    assert file.is_file
    assert file.user == "root"
    assert file.group == "root"

def test_motd_output(host):
    command = host.run(composer_bin_file)
    assert command.succeeded
    assert command.stderr == ""
    print(f"\n{command.stdout}")
