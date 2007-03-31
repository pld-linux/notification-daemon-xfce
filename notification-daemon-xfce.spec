# TODO:
# - cleanup and rel1
Summary:	Notification Daemon for xfce4
Summary(pl.UTF-8):	Demon powiadomień dla xfce4
Name:		notification-daemon-xfce
Version:	0.3.6
Release:	0.1
License:	GPL v2+
Group:		Applications/System
Source0:	http://goodies.xfce.org/releases/%{name}/%{name}-0.3.6.tar.bz2
# Source0-md5:	bd696b1198904c452c3dec9fcbcea1f7
Patch0:		%{name}-dbus.patch
URL:		http://goodies.xfce.org/projects/applications/notification-daemon-xfce
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libsexy-devel >= 0.1.8
BuildRequires:	libxfcegui4-devel
BuildRequires:	libxfce4util-devel
Requires:	dbus >= 0.91
BuildRoot:	%{_tmppath}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure 
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
%{_desktopdir}/notification-settings.desktop
%{_datadir}/dbus-1/services/*.service
%{_iconsdir}/hicolor/*/apps/notification-settings.png
