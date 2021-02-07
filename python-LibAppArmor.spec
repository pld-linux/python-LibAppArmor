Summary:	AppArmor Python 2 bindings
Summary(pl.UTF-8):	Dowiązania do AppArmor dla Pythona 2
Summary(pt_BR.UTF-8):	Módulos Python 2 para acessar os recursos do AppArmor
Name:		python-LibAppArmor
# NOTE: versions >= 3.0 support python3 only
Version:	2.13.4
Release:	1
Epoch:		1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://launchpad.net/apparmor/2.13/%{version}/+download/apparmor-%{version}.tar.gz
# Source0-md5:	a50b793a3362551f07733be3df9c328f
URL:		http://wiki.apparmor.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1.4
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc >= 5:3.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	swig-python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppArmor Python 2 bindings.

%description -l pl.UTF-8
Dowiązania do AppArmor dla Pythona 2.

%description -l pt_BR.UTF-8
Módulos Python 2 para acessar os recursos do AppArmor.

%prep
%setup -q -n apparmor-%{version}

%build
cd libraries/libapparmor
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	PYTHON=%{__python} \
	--with-python \
	--without-ruby \
	--without-perl

%{__make} -C swig/python -j1 \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 -C libraries/libapparmor/swig/python install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/LibAppArmor
%attr(755,root,root) %{py_sitedir}/LibAppArmor/_LibAppArmor.so
%{py_sitedir}/LibAppArmor/__init__.py[co]
%{py_sitedir}/LibAppArmor/LibAppArmor.py[co]
%{py_sitedir}/LibAppArmor-*.egg-info
