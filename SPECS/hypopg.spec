###############
# Set metadata
###############
%global _version 0.0.4


Name:           hypopg%{suffix}
Version:        %{_version}
Release:        1%{?dist}
Summary:        HypoPG is a PostgreSQL extension adding support for hypothetical indexes

Group:          Development/Tools
License:        PostgreSQL License
URL:            https://github.com/dalibo/hypopg
Source:         https://github.com/dalibo/hypopg/archive/0.0.4.tar.gz

Obsoletes:      hypopg%{suffix} <= 0.03
Provides:       hypopg%{suffix} = 0.04

%description
This software is EXPERIMENTAL and therefore NOT production ready. Use at your own risk.
New features:   adds support for BRIN indexes (for postgres 9.5+)
                handles index on predicate
                handles index storage parameters for supported index methods. For now, this means..
                - fillfactor for btree indexes
                - pages_per_range for brin indexes


HypoPG is a PostgreSQL extension adding support for hypothetical indexes.

This project is sponsored by Dalibo.

#####################
# Build requirements
#####################
BuildRoot: %(mktemp -ud %{_tmppath}/build/%{name}-%{version}-%{release}-XXXXXX)

########################################################
# PREP and SETUP
# The prep directive removes existing build directory
# and extracts source code so we have a fresh code base
# -n defines the name of the directory
#######################################################


%prep


#%setup -q -n %{name}-%{version}
%setup -n hypopg-0.0.4

#######################################################

%build
#%%configure
make %{?_smp_mflags}

#######################################################

%install
%make_install

mkdir -p %{_buildrootdir}/etc/profile.d

echo 'export PATH=$PATH:%{pg_dir}/bin/' >> %{_buildrootdir}/etc/profile.d/hypopg.sh
echo 'export USE_PGXS=1' >> %{_buildrootdir}/etc/profile.d/hypopg.sh
source %{_buildrootdir}/etc/profile.d/hypopg.sh

#######################################################
%files
%defattr(-,root,root,-)
/usr/pgsql-9.5/doc/extension/README.md
/usr/pgsql-9.5/lib/hypopg.so
/usr/pgsql-9.5/share/extension/hypopg--0.0.4.sql
/usr/pgsql-9.5/share/extension/hypopg.control



%changelog

