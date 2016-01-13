#!/usr/bin/env bash

## make necessary changes when performing the build in the admin terminal

sudo yum -y groupinstall 'Development Tools'
sudo yum -y install yum localinstall http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-centos94-9.4-1.noarch.rpm
sudo yum -y install postgresql9*
sudo yum -y install java-1.7.0*
sudo yum -y install tree
sudo yum -y install vim

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
       SCRIPTPATH=/vagrant
   fi
  
  mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
 #ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros
cd $HOME/rpmbuild/SOURCES
wget https://github.com/dalibo/hypopg/archive/0.0.4.tar.gz
