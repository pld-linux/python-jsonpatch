#
# Conditional build:
%bcond_with	tests	# do perform "make test" (broken - tests.js file missing)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Apply JSON-Patches (RFC 6902)
Name:		python-jsonpatch
Version:	1.16
Release:	5
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
# Source0-md5:	8ef1ceb00dcf992c9e43611f698f9279
URL:		https://pypi.python.org/pypi/jsonpatch
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-jsonpointer >= 1.9
%endif
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-jsonpointer >= 1.9
%endif
%endif
Requires:	python-jsonpointer >= 1.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to apply JSON Patches according to RFC 6902.

%package -n python3-jsonpatch
Summary:	Apply JSON-Patches (RFC 6902)
Group:		Libraries/Python
Requires:	python3-jsonpointer >= 1.9

%description -n python3-jsonpatch
Library to apply JSON Patches according to RFC 6902.

%package -n jsonpatch
Summary:	Apply JSON-Patches (RFC 6902)
Group:		Libraries/Python
%if %{with python3}
Requires:	python3-jsonpatch = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n jsonpatch
Library to apply JSON Patches according to RFC 6902.


%prep
%setup -q -n jsonpatch-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
# otherwise python2 scripts would be used
rm -f $RPM_BUILD_ROOT%{_bindir}/* || :

%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%{py_sitescriptdir}/jsonpatch.py[co]
%{py_sitescriptdir}/jsonpatch-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jsonpatch
%defattr(644,root,root,755)
%doc AUTHORS README.md
%{py3_sitescriptdir}/jsonpatch.py
%{py3_sitescriptdir}/__pycache__/*
%{py3_sitescriptdir}/jsonpatch-%{version}-py*.egg-info
%endif

%files -n jsonpatch
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/jsonpatch
%attr(755,root,root) %{_bindir}/jsondiff
