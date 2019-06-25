# Ansible role datadog-check-lynis

[![Build Status](https://img.shields.io/travis/infothrill/ansible-role-datadog-check-lynis/master.svg?label=travis_master)](https://travis-ci.org/infothrill/ansible-role-datadog-check-lynis)
[![Build Status](https://img.shields.io/travis/infothrill/ansible-role-datadog-check-lynis/develop.svg?label=travis_develop)](https://travis-ci.org/infothrill/ansible-role-datadog-check-lynis)
[![Updates](https://pyup.io/repos/github/infothrill/ansible-role-datadog-check-lynis/shield.svg)](https://pyup.io/repos/github/infothrill/ansible-role-datadog-check-lynis/)
[![Ansible Role](https://img.shields.io/ansible/role/22962.svg)](https://galaxy.ansible.com/infothrill/datadog-check-lynis/)


An [Ansible](http://www.ansible.com) role to install a
[Datadog](https://www.datadoghq.com) agent check for
[Lynis](https://cisofy.com/lynis/), an open source security auditing tool.

## Quick howto

requirements.yml:

	- src: Datadog.datadog
	  version: 1.6.1
	- src: infothrill.datadog-check-lynis
	  version: v1.1.0

Install:

	ansible-galaxy install -r requirements.yml -p ./roles/

Playbook:

    - hosts: servers
        roles:
		    - role: Datadog.datadog
		    - role: ansible-role-datadog-check-lynis

To configure the check, please use the Datadog.datadog role and add an entry
in the `checks` dictionary there:

	  lynis:
	    init_config:
	    instances:
          - metrics:
		      - hardening_index
		      - installed_packages
		      - lynis_tests_done
		    report: /var/log/lynis/report.dat

## Role Variables

|       variable             | default  | description     |
|:--------------------------:|:--------:|:----------------|
| ddagent_user               | dd-agent | agent user      |
| ddagent_group              | dd-agent | agent group     |

## Dependencies

In principle, this role can be run standalone, however it is only tested together
with the role [Datadog.datadog](https://galaxy.ansible.com/Datadog/datadog/).
The recommended approach would be to:

* install datadog using the upstream role
* configure the check using the upstream role
* run this role to deploy the check plugin only

## License

MIT

## Author Information

This role was created in 2017 by Paul Kremer.


## Changes

### v1.1.x

* drop support for ansible EOL versions 2.2, 2.3
* add testing support for ansible 2.8

### v1.1.0

* Auto-detect agent5/6 configuration directory (backwards compatible)
* Add support for EL 6,7
* Optimize molecule test

### v1.0.3

* Upgrade molecule
* Fix meta/main.yml to reflect correct values

### v1.0.2

* remove ansible 2.1 and add ansible 2.5
* upgrade molecule

### v1.0.1

* remove unused files and outcommented code

### v1.0

* initial release
