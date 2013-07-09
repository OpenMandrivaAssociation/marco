%define oname mate-window-manager
%define name  marco
%define major 0
%define libname %mklibname marco-private %{major}
%define develname %mklibname -d marco-private
%define startup_notification_version 0.4

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:       Mate window manager
Name:          %{name}
Version:       1.6.2
Release:       1
URL:           http://www.mate-desktop.org/
Source0:       http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz
# use oxygen as our default theme
Source1:       http://gnome-look.org/CONTENT/content-files/76582-Oxygen_Accurate_Installation_Files.tar.bz2
License:       GPLv2+
Group:         Graphical desktop/Other

BuildRequires: intltool
BuildRequires: mate-common
BuildRequires: mate-dialogs
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(libcanberra-gtk)
BuildRequires: pkgconfig(libgtop-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(pangoxft)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: libmesaglu-devel

Requires:      mate-dialogs
Provides:      %{oname} = %{version}-%{release}


%description
The Mate window manager integrates nicely with MATE.

%package -n %{libname}
Summary:        Libraries for Mate window manager
Group:          System/Libraries

%description -n %{libname}
This package contains libraries used by Mate window manager.

%package -n %{develname}
Summary:        Libraries and include files with Mate window manager
Group:          Development/C
Requires:	%{libname} = %{version}
Provides:	%{oname}-devel = %{version}-%{release}

%description -n %{develname}
This package provides the necessary development libraries and include 
files to allow you to develop with Mate window manager.


%prep
%setup -q -n %{oname}-%{version} -b1
%apply_patches

pushd "../Oxygen Accurate Installation Files"
tar xf OxygenAccurate.tar.gz
popd

%build
%configure2_5x \
        --disable-static \
        --disable-scrollkeeper

%make

%install
%makeinstall_std

%find_lang %{name}

rm -fr %buildroot%{_libdir}/*.la

pushd "../Oxygen Accurate Installation Files/Oxygen Accurate"
mkdir -p %{buildroot}%{_datadir}/themes/oxygnome
cp -fr metacity-1 %{buildroot}%{_datadir}/themes/oxygnome/metacity-1
popd

%files -f marco.lang
%doc README COPYING NEWS HACKING 
%{_bindir}/*
%{_datadir}/mate-control-center/keybindings/50-marco-*.xml
%{_datadir}/applications/marco.desktop
%{_datadir}/mate/wm-properties/marco-wm.desktop
%{_datadir}/%{oname}
%{_datadir}/glib-2.0/schemas/org.mate.marco.gschema.xml
%{_datadir}/MateConf/gsettings/marco.convert
%{_datadir}/themes/*
%{_mandir}/man1/*
%{_datadir}/mate/help/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

