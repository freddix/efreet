Summary:	Enlightenment Foundation Library
Name:		efreet
Version:	1.7.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	066cb170eb514a6020dce85a22a76648
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Efreet is a library designed to help apps work several of the
Freedesktop.org standards regarding Icons, Desktop files and Menus.

%package devel
Summary:	Header files for efreet library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for efreet library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-install-examples	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/efreet_*
%dir %{_libdir}/efreet
%attr(755,root,root) %{_libdir}/efreet/efreet_desktop_cache_create
%attr(755,root,root) %{_libdir}/efreet/efreet_icon_cache_create

%attr(755,root,root) %ghost %{_libdir}/libefreet*.so.1
%attr(755,root,root) %{_libdir}/libefreet*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libefreet*.so
%{_includedir}/efreet-1
%{_pkgconfigdir}/efreet*.pc

