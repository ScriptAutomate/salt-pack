%if ( "0%{?dist}" == "0.amzn1" )
%global with_explicit_python27 1
%global pybasever 2.7 
%global __python_ver 27
%else

%if ! (0%{?rhel} >= 6 || 0%{?fedora} > 12)
%global with_python26 1
%define pybasever 2.6 
%define __python_ver 26
%endif

%endif


Name: winexe
Version: 1.1
Release: 1b787d2.2%{?dist}
Summary: Remote Windows command executor.


Group: Applications/System
License: GPLv3
URL: http://sourceforge.net/projects/winexe/
Source0: %{name}-%{version}.tar.gz
Patch0: samba4-libs.patch
Patch1: samba42-debug.patch

BuildRequires: gcc
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: popt-devel
BuildRequires: openldap-devel
Requires: samba4-libs >= 4.2.0

%if (0%{?rhel} >= 7 || "0%{?dist}" == "0.amzn1")
BuildRequires: python%{?__python_ver}-devel
Requires: glibc >= 2.17 

%else
%if (0%{?rhel} == 6)

BuildRequires: rpm-build
BuildRequires: pkgconfig
BuildRequires: libtalloc-devel
BuildRequires: samba4-devel >= 4.2.0
Requires: glibc >= 2.12

%endif
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-build

%description
Winexe remotely executes commands on Windows
NT/2000/XP/2003/Vista/7/2008/8/2012 systems from GNU/Linux.


%prep
cd ../SOURCES
tar -xzvf winexe-1.1.tar.gz

%setup 
%patch0 -p0 -b .patch0


# Disable debug only for EL >= 7 because of https://sourceforge.net/p/winexe/bugs/77/
# Patch from Michael Stowe: https://sourceforge.net/u/mstowe/winexe/ci/master/tree/
%if 0%{?rhel} >= 7
%patch1 -p0 -b .patch1
%endif

%build
cd source
./waf configure build
## ./waf --samba-dir=../../samba configure build


%install
echo %{buildroot}
rm -rf %{buildroot}
%__install -d %{buildroot}/usr/bin
%__install source/build/winexe %{buildroot}/usr/bin


%clean
rm -rf %{buildroot}


%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/winexe


%changelog
* Tue Apr 25 2017 SaltStack Packaging Team <packaging@saltstack.com> - 1.1-1b787d2-2
- Update to support minimum samba 4.2 or greater
- Change waf script so it can use the new samba 4.x library names
- Support CentOS7 again thanks to a patch from Michel Stowe at
  https://sourceforge.net/u/mstowe/winexe/ci/master/tree

* Wed Oct 26 2016 SaltStack Packaging Team <packaging@saltstack.com> - 1.1-b787d2-1
- Update to support Redhat 6 and native Amazon Linux

* Sun Feb 14 2016 Randy Thompson <randy@heroictek.com> - 1.1-b787d2
- b787d2a2c4b1abc3653bad10aec943b8efcd7aab from git://git.code.sf.net/p/winexe/winexe-waf
- a6bda1f2bc85779feb9680bc74821da5ccd401c5 from git://git.samba.org/samba.git
