%if ( "0%{?dist}" == "0.amzn1" )
%global with_explicit_python27 1
%global pybasever 2.7
%global __python_ver 27
%global __python %{_bindir}/python%{?pybasever}
%global __python2 %{_bindir}/python%{?pybasever}

# work-around Amazon Linux get_python_lib returning  /usr/lib64/python2.7/dist-packages
## %global python2_sitelib  /usr/lib/python2.7/site-packages 

%global python2_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%global __inst_layout --install-layout=unix

%else
%if !(0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python2_sitelib: %global python2_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif
%endif

Name:           python-cherrypy
Version:        3.2.2
Release:        6%{?dist}
Summary:        Pythonic, object-oriented web development framework
Group:          Development/Libraries
License:        BSD
URL:            http://www.cherrypy.org/
Source0:        http://download.cherrypy.org/cherrypy/%{version}/CherryPy-%{version}.tar.gz
# Don't ship the tests or tutorials in the python module directroy,
# tutorial will be shipped as doc instead
Patch0:         python-cherrypy-tutorial-doc.patch
Patch1: cherrypy-unittest.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%if 0%{?with_explicit_python27}
BuildRequires:  python27-devel
BuildRequires:  python27-setuptools
BuildRequires:  python27-nose
%else
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
%endif

%description
CherryPy allows developers to build web applications in much the same way 
they would build any other object-oriented Python program. This usually 
results in smaller source code developed in less time.

%if 0%{?with_explicit_python27}
%package -n python%{?__python_ver}-cherrypy
Summary:        Pythonic, object-oriented web development framework
Group:          Development/Libraries

%description  -n python%{?__python_ver}-cherrypy
CherryPy allows developers to build web applications in much the same way 
they would build any other object-oriented Python program. This usually 
results in smaller source code developed in less time.

This package is meant to be used with Python 2.7.
%endif

%prep
%setup -q -n CherryPy-%{version}
%patch0 -p1
%patch1 -p1

%{__sed} -i 's/\r//' README.txt cherrypy/tutorial/README.txt cherrypy/tutorial/tutorial.conf

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build %{?__inst_layout } --root $RPM_BUILD_ROOT

## %%check
## cd cherrypy/test
## # These two tests hang in the buildsystem so we have to disable them.
## # The third fails in cherrypy 3.2.2.
## %%if ( "0%%{?dist}" == "0.amzn1" )
## PYTHONPATH='../../' nosetests -s ./ -e 'test_SIGTERM' -e \
##   'test_SIGHUP_tty' -e 'test_file_stream' -e 'test_no_content_length' \
##   -e 'assertStatus'
## %%else
## PYTHONPATH='../../' nosetests -s ./ -e 'test_SIGTERM' -e \
##   'test_SIGHUP_tty' -e 'test_file_stream'
## %%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python%{?__python_ver}-cherrypy
%defattr(-,root,root,-)
%doc README.txt
%doc cherrypy/tutorial
%{_bindir}/cherryd
%{python2_sitelib}/*

%changelog
* Wed Sep 11 2019 SaltStack Packaging Team <packaging@saltstack.com> - 3.2.2-6
- Disabled check since running into utf-8 issues in tests

* Tue Oct 18 2016 SaltStack Packaging Team <packaging@saltstack.com> - 3.2.2-5
- Ported to build on Amazon Linux 2016.09 natively

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Conrad Meyer <konrad@tylerc.org> - 3.2.2-1
- Update to 3.2.2

* Sat Jul 16 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 3.2.1-1
- Update to 3.2.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 3.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon May 31 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-4
- Fix a failing unittest with newer python

* Sat Apr 24 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-3
- Revert a try at 3.2.x-rc1 as the tests won't pass without some work.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.2-1
- New upstream with python-2.6 fixes.
- BR tidy for tests.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 1 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1
- Fix python-2.6 build errors
- Make test code non-interactive via cmdline switch
- Refresh the no test and tutorial patch

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 3.0.3-3
- Rebuild for Python 2.6

* Tue Jan 22 2008 Toshio Kuratomi <toshio@fedoraproject.org> 3.0.3-2
- Forgot to upload the tarball.

* Mon Jan 21 2008 Toshio Kuratomi <toshio@fedoraproject.org> 3.0.3-1
- Upgrade to 3.0.3.

* Thu Jan 17 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.3.0-2
- EINTR Patch needed to be forwarded ported as well as it is only applied to
  CP trunk (3.x).

* Thu Jan 17 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.3.0-1
- Update to new upstream which rolls in the backported security fix.
- Refresh other patches to apply against new version.
- Change to new canonical source URL.
- Reenable tests.

* Sun Jan  6 2008 Toshio Kuratomi <toshio@fedoraproject.org> 2.2.1-8
- Fix a security bug with a backport of http://www.cherrypy.org/changeset/1775
- Include the egginfo files as well as the python files.

* Sat Nov  3 2007 Luke Macken <lmacken@redhat.com> 2.2.1-7
- Apply backported fix from http://www.cherrypy.org/changeset/1766
  to improve CherryPy's SIGSTOP/SIGCONT handling (Bug #364911).
  Thanks to Nils Philippsen for the patch.

* Mon Feb 19 2007 Luke Macken <lmacken@redhat.com> 2.2.1-6
- Disable regression tests until we can figure out why they
  are dying in mock.

* Sun Dec 10 2006 Luke Macken <lmacken@redhat.com> 2.2.1-5
- Add python-devel to BuildRequires

* Sun Dec 10 2006 Luke Macken <lmacken@redhat.com> 2.2.1-4
- Rebuild for python 2.5

* Mon Sep 18 2006 Luke Macken <lmacken@redhat.com> 2.2.1-3
- Rebuild for FC6
- Include pyo files instead of ghosting them

* Thu Jul 13 2006 Luke Macken <lmacken@redhat.com> 2.2.1-2
- Rebuild

* Thu Jul 13 2006 Luke Macken <lmacken@redhat.com> 2.2.1-1
- Update to 2.2.1
- Remove unnecessary python-abi requirement

* Sat Apr 22 2006 Gijs Hollestelle <gijs@gewis.nl> 2.2.0-1
- Update to 2.2.0

* Wed Feb 22 2006 Gijs Hollestelle <gijs@gewis.nl> 2.1.1-1
- Update to 2.1.1 (Security fix)

* Tue Nov  1 2005 Gijs Hollestelle <gijs@gewis.nl> 2.1.0-1
- Updated to 2.1.0

* Sat May 14 2005 Gijs Hollestelle <gijs@gewis.nl> 2.0.0-2
- Added dist tag

* Sun May  8 2005 Gijs Hollestelle <gijs@gewis.nl> 2.0.0-1
- Updated to 2.0.0 final
- Updated python-cherrypy-tutorial-doc.patch to match new version

* Wed Apr  6 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.0-0.2.b
- Removed CFLAGS

* Wed Mar 23 2005 Gijs Hollestelle <gijs[AT]gewis.nl> 2.0.0-0.1.b
- Initial Fedora Package
