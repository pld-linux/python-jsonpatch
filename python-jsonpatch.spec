#
# Conditional build:
%bcond_with	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Apply JSON-Patches (RFC 6902)
Summary(pl.UTF-8):	Nakładanie łat JSON-Patch (RFC 6902)
Name:		python-jsonpatch
Version:	1.33
Release:	4
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
# Source0-md5:	ed3e8eaa5cce105ad02509d185f0889f
URL:		https://pypi.python.org/pypi/jsonpatch
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-jsonpointer >= 1.9
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-jsonpointer >= 1.9
%endif
%endif
Requires:	python-jsonpointer >= 1.9
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library to apply JSON Patches according to RFC 6902.

%description -l pl.UTF-8
Biblioteka do nakładania łat JSON Patch zgodnie z RFC 6902.

%package -n python3-jsonpatch
Summary:	Apply JSON-Patches (RFC 6902)
Summary(pl.UTF-8):	Nakładanie łat JSON-Patch (RFC 6902)
Group:		Libraries/Python
Requires:	python3-jsonpointer >= 1.9
Requires:	python3-modules >= 1:3.7

%description -n python3-jsonpatch
Library to apply JSON Patches according to RFC 6902.

%description -n python3-jsonpatch -l pl.UTF-8
Biblioteka do nakładania łat JSON Patch zgodnie z RFC 6902.

%package -n jsonpatch
Summary:	Apply JSON-Patches (RFC 6902)
Summary(pl.UTF-8):	Nakładanie łat JSON-Patch (RFC 6902)
Group:		Applications/File
%if %{with python3}
Requires:	python3-jsonpatch = %{version}-%{release}
%else
Requires:	%{name} = %{version}-%{release}
%endif

%description -n jsonpatch
Utilities to apply JSON Patches according to RFC 6902.

%description -n jsonpatch -l pl.UTF-8
Narzędzia do nakładania łat JSON Patch zgodnie z RFC 6902.

%prep
%setup -q -n jsonpatch-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} tests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} tests.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%if %{with python3}
# otherwise python2 scripts would be used
%{__rm} $RPM_BUILD_ROOT%{_bindir}/*
%endif
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%{py_sitescriptdir}/jsonpatch.py[co]
%{py_sitescriptdir}/jsonpatch-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-jsonpatch
%defattr(644,root,root,755)
%doc AUTHORS README.md
%{py3_sitescriptdir}/jsonpatch.py
%{py3_sitescriptdir}/__pycache__/jsonpatch.cpython-*.py[co]
%{py3_sitescriptdir}/jsonpatch-%{version}-py*.egg-info
%endif

%files -n jsonpatch
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsondiff
%attr(755,root,root) %{_bindir}/jsonpatch
