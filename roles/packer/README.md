# ansible-role-packer

This role provide install packer on your host.


## Supported platforms:

```yaml
- name: EL
  versions:
    - 8
    - 7
- name: Debian
  versions:
    - buster
    - stretch
- name: Ubuntu
  versions:
    - disco
    - bionic
    - trusty
    - precise
- name: Alpine
  versions:
    - any
- name: MacOSX
  versions:
    - 10.10
    - 10.11
    - 10.12
    - 10.13
```

## Role Variables

This role has multiple variables. The defaults for all these variables are the following:

```yaml
---

# Possible values: https://releases.hashicorp.com/packer/index.json
# Default: latest
packer_version: latest

# Packer destination path
packer_path: /usr/local/bin/
```

## Dependencies

None

## Example Playbook

This is a sample playbook file for deploying the Ansible Galaxy packer role in a localhost and installing the latest version of packer.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - role: redbeard28.packer
```

This role can also install a specific version of packer.

```yaml
---
- hosts: localhost
  become: true
  roles:
    - role: redbeard28.packer
      vars:
        packer_version: 1.5.1

```


## License

GPLv3

## Author Information

This role was created in 2018 by redbeard28.

