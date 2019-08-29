%define url_ver	%(echo %{version} | cut -d. -f1,2)

%define _disable_rebuild_configure 1

Name:		xfce4-calculator-plugin
Summary:	Calculator pluging for the Xfce4 panel
Version:	0.7.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-calculator-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-calculator-plugin/%{url_ver}/xfce4-calculator-plugin-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
Requires:	xfce4-panel

%description
xfce4-calculator-plugin is a calculator plugin for the Xfce4 panel.

%prep
%setup -q

%build
%configure
%xdt_autogen
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README TODO
%{_libdir}/xfce4/panel/plugins/libcalculator.so
%{_iconsdir}/hicolor/*/apps/xfce4-calculator-plugin.png
%{_datadir}/xfce4/panel/plugins/calculator.desktop
