Summary:	Notification Daemon for xfce4
Summary(pl.UTF-8):	Demon powiadomień dla xfce4
Name:		notification-daemon-xfce
Version:	0.3.7
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://goodies.xfce.org/releases/notification-daemon-xfce/%{name}-%{version}.tar.bz2
# Source0-md5:	ef4a4977875d97a5237b316d5d592176
URL:		http://goodies.xfce.org/projects/applications/notification-daemon-xfce
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	intltool
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libsexy-devel >= 0.1.8
BuildRequires:	libxfce4util-devel >= 4.3.90
BuildRequires:	libxfcegui4-devel >= 4.3.90
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce-mcs-manager-devel >= 4.2.2
Requires:	dbus >= 0.91
Provides:	dbus(org.freedesktop.Notifications)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A daemon that displays passive pop-up notifications as per the Desktop
Notifications spec.

This is a reimplementation of the oryginal GNOME daemon for xfce4.

%description -l pl.UTF-8
Demon wyświetlający pasywne wyskakujące (pop-up) powiadomienia zgodnie
ze specyfikacją Desktop Notifications.

To jest reimplementacja oryginalnego demona dla GNOME dla xfce4.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gradient-look
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/notification-daemon-1.0/engines/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/notification-settings
%dir %{_libdir}/notification-daemon-xfce-1.0
%dir %{_libdir}/notification-daemon-xfce-1.0/engines
%attr(755,root,root) %{_libdir}/notification-daemon-xfce-1.0/engines/*.so
%attr(755,root,root) %{_libdir}/notification-daemon-xfce
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/notification_settings.so
%{_datadir}/dbus-1/services/*.service
%{_desktopdir}/notification-settings.desktop
%{_iconsdir}/hicolor/*/apps/notification-settings.png
