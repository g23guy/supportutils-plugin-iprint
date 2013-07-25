#
# spec file for package supportutils-plugin-iprint (Version 1.0-1)
#
# Copyright (C) 2010 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-iprint
URL:          https://code.google.com/p/supportutils-plugin-iprint/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.1
Release:      8
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for Novell iPrint
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource
Requires:     supportconfig-plugin-tag

%description
Extends supportconfig functionality to include system information about 
Novell iPrint. The supportconfig saves the plugin output to plugin-iPrint.txt.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-iprint/issues/list

Authors:
--------
    Jeremy Meldrum <jmeldrum@novell.com>
    Jason Record <jrecord@novell.com>

%prep
%setup -q
%build
gzip -9f iprint-plugin.8
gzip -9f iPrintInfo.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -d $RPM_BUILD_ROOT/sbin
install -d $RPM_BUILD_ROOT/etc/opt/novell/iprint-plugin
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 iPrint $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -m 0544 iPrintInfo $RPM_BUILD_ROOT/sbin
install -m 0600 iprint-plugin.conf $RPM_BUILD_ROOT/etc/opt/novell/iprint-plugin
install -m 0644 iprint-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/iprint-plugin.8.gz
install -m 0644 iPrintInfo.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/iPrintInfo.8.gz

%files
%defattr(-,root,root)
/usr/lib/supportconfig
/usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/*
/sbin/iPrintInfo
/etc/opt/novell
%attr(700,root,root) /etc/opt/novell/iprint-plugin
%verify(mode) %attr(600,root,root) %config /etc/opt/novell/iprint-plugin/iprint-plugin.conf
/usr/share/man/man8/iprint-plugin.8.gz
/usr/share/man/man8/iPrintInfo.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-iprint

