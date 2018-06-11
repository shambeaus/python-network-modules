# python-network-modules

Ths repo is a collection of example usages of the common python network modules

## Setup

- python3
- clone repo to local machine
- Setup virtual environment and install packages with pipenv

```
pipenv install
pipenv shell
```

# Examples:

## Ansible

 - WIP...

## Ciscoconfparse

 - **asa_object_parse** - parse through running config of an ASA and return a dictionary with object-group and object members
 - **config_section** - match on a regex parent object and return that section from running config
 - **parent_child** - use cisconfparse 'parentspec/childspec' to return list of non-shut interfaces
 - **remove_config** - use ciscoconfparse to modify configuration. matches on parent object regex and removes config block. Can be returned to a variable or saved as a new file.

## Jinja

- WIP...

## Napalm

 - **get_facts** - basic fact collection
 - TODO: add more napalm examples

## Netmiko

 - **asa_config** - send a set of configuration commands to device using netmiko, then save config
 - **asa_show** - send set of show commands to device and print results
 - **asa_threading** - use queue and threading to send commands to a list of devices
 - **asa_scp_interactive** - use netmiko 'file_transfer' to scp files to/from remote devices
 - **threading_code_upload** - further example of threading using 'filetransfer' to copy files to list of devices

## pexpect

- **pxssh** - open ssh connection to remote device issue command and print results
- **pxssh_func** - function to pass connection detail and command, run command on remote host and return result
- **ssh_spwan** - using pexpect spawn to open session to remote device, use '.expect' and '.before' to collect output

## TextFSM
- WIP...

