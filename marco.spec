%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define oname mate-window-manager
%define major 1
%define libname %mklibname marco-private %{major}
%define devname %mklibname -d marco-private

Summary:	Mate window manager
Name:		marco
Version:	1.14.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		http://www.mate-desktop.org/
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	zenity
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcanberra-gtk)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(pangoxft)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xrender)
Requires:	zenity
%rename	%{oname}

%description
The Mate window manager integrates nicely with MATE.

%package -n %{libname}
Summary:	Libraries for Mate window manager
Group:		System/Libraries

%description -n %{libname}
This package contains libraries used by Mate window manager.

%package -n %{devname}
Summary:	Libraries and include files with Mate window manager
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the necessary development libraries and include 
files to allow you to develop with Mate window manager.

%prep
%setup -q 

%build
%configure --with-gtk=3.0

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

# remove unneeded converter
rm -fr %{buildroot}%{_datadir}/MateConf

%files -f marco.lang
%doc README COPYING NEWS HACKING 
%{_bindir}/*
%{_datadir}/applications/marco.desktop
%{_datadir}/glib-2.0/schemas/org.mate.marco.gschema.xml
%{_datadir}/%{name}
%{_datadir}/mate/wm-properties/marco-wm.desktop
%{_datadir}/mate-control-center/keybindings/50-marco-*.xml
%{_datadir}/themes/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libmarco-private.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%{_libdir}/libmarco-private.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

