RPM Spec file for HypoPG

**Description**:
HypoPG is a PostgreSQL extension adding support for hypothetical indexes.
This project is sponsored by Dalibo.

## Installation

### Build the RPM using Vagrant

1. Once the repo has been cloned, run "vagrant up" to create the bulid VM
2. Run "vagrant ssh" to connect
3. CD to ~/rpmbuild
4. Run "rpmbuild -ba SPECS/hypopg.spec"


### Install the RPM

Install the built RPM by running "sudo yum install RPMS/x86_64/hypopg.rpm"

## Configuration

Edit the SPEC file to make changes to the build configuration.

## Usage

hypopg will be installed in /usr/bin


