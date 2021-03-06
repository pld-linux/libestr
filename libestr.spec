#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Some essential string manipulation functions
Summary(pl.UTF-8):	Kilka podstawowych funkcji do manipulacji łańcuchami
Name:		libestr
Version:	0.1.11
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://libestr.adiscon.com/files/download/%{name}-%{version}.tar.gz
# Source0-md5:	1f25a2332750d4bfacfb314235fedff0
URL:		https://libestr.adiscon.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libestr is a library that contains some essential string manipulation
functions.

%description -l pl.UTF-8
libestr jest biblioteką zawierającą kilka podstawowych funkcji do
manipulacji łańcuchami.

%package devel
Summary:	Header files for libestr library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libestr
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libestr library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libestr.

%package static
Summary:	Static libestr library
Summary(pl.UTF-8):	Statyczna biblioteka libestr
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libestr library.

%description static -l pl.UTF-8
Statyczna biblioteka libestr.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies, pkgconfig file present
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libestr.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libestr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libestr.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libestr.so
%{_includedir}/libestr.h
%{_pkgconfigdir}/libestr.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libestr.a
%endif
