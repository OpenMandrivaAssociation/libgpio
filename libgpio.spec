##### GENERAL STUFF #####

%define major	0
%define libname	%mklibname gpio %{major}

Summary:	I/O library for GPhoto 2.x
Name:		libgpio
Version:	0.0.2
Release:	%mkrel 14
License:	LGPL
Group:		Graphics

##### SOURCE FILES #####

Source: libgpio.tar.bz2
Patch0: libgpio-alpha.patch
Patch1: libgpio-includes.patch
Patch2: libgpio-lib64.patch

##### ADDITIONAL DEFINITIONS #####

BuildRequires:	libusb-devel
BuildRoot: %{_tmppath}/%{name}-buildroot

##### SUB-PACKAGES #####

%description
libgpio is a library for different I/O operations done by GPhoto 2.0

%package -n %{libname}
Summary:	I/O library for GPhoto 2.x
Group:		Graphics
Provides:	libgpio = %{version}-%{release}

%description -n %{libname}
libgpio is a library for different I/O operations done by GPhoto 2.0

%package -n %{libname}-devel
Summary: Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} = %{version}-%{release}
Provides:	libgpio-devel = %{version}-%{release}
Group:		Graphics

%description -n %{libname}-devel
This package contains all files which one needs to compile programs using
the "%{libname}" library.


##### PREP #####

%prep
%setup -q -n libgpio
%patch -p1 -b .alpha
%patch1 -p1 -b .includes
%patch2 -p1 -b .lib64

##### BUILD #####

%build
# "autogen" is needed because we have a CVS snapshot.
# (cjw) do not run autogen.sh directly
libtoolize --copy --force
aclocal-1.7
autoheader
automake-1.7 -a -c --gnu
autoconf

%configure
%make

##### INSTALL #####

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# Install the README files of the source tarball in the doc directory
#cp *.txt $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}


##### PRE/POST INSTALL SCRIPTS #####

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

##### CLEAN UP #####

%clean
rm -rf $RPM_BUILD_ROOT


##### FILE LISTS FOR ALL BINARY PACKAGES #####

##### %{libname}
%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%{_libdir}/gpio/*.so.*

##### %{libname}-devel
%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/*.sh
%{_libdir}/gpio/*.so
%{_libdir}/gpio/*.la
%{_libdir}/gpio/*.a
%{_bindir}/*
%{_includedir}/gpio/*

##### CHANGELOG #####

