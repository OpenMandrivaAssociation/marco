%define mate_ver	%(echo %{version}|cut -d. -f1,2)

%define oname mate-window-manager
%define major 2
%define libname %mklibname marco-private
%define devname %mklibname marco-private -d
%define oldlibname %mklibname marco-private 2

Summary:	Mate window manager
Name:		marco
Version:	1.28.1
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/Other
Url:		https://www.mate-desktop.org/
Source0:	https://pub.mate-desktop.org/releases/%{mate_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf-archive
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(pangox)
BuildRequires:	pkgconfig(pangoxft)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xpresent)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xres)
BuildRequires:	zenity-gtk
BuildRequires:	yelp-tools

Requires:	zenity-gtk

%rename		%{oname}

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

Marco is a simple window manager that integrates nicely with MATE.

%files -f marco.lang
%doc README COPYING HACKING NEWS
%{_bindir}/*
%{_datadir}/applications/marco.desktop
%{_datadir}/glib-2.0/schemas/org.mate.marco.gschema.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/mate/wm-properties/marco-wm.desktop
%{_datadir}/mate-control-center/keybindings/50-marco-*.xml
%{_datadir}/themes/*
%doc %{_mandir}/man1/*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for Mate window manager
Group:		System/Libraries
License:	LGPLv2+
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
This package contains libraries used by %{name}.

%files -n %{libname}
%doc COPYING
%{_libdir}/libmarco-private.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and include files with Mate window manager
Group:		Development/C
License:	LGPLv2+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and includes files for developing programs
based on %{name}.

%files -n %{devname}
%doc ChangeLog COPYING
%{_includedir}/*
%{_libdir}/pkgconfig/libmarco-private.pc
%{_libdir}/libmarco-private.so

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
#NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-schemas-compile

# fix rpmlint unused-direct-shlib-dependency warning
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%make_install

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/marco.desktop

