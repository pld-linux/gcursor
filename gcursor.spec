Summary:	gcursor - a little program to change youre Xcursor
Summary(pl):	gcursor - ma³y program do zmiany kursora
Name:		gcursor
Version:	0.061
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.qballcow.nl/programs/gcursor/%{name}-%{version}.tar.gz
# Source0-md5:	233810996bc7f69879f8978c523ae723
Patch0:		%{name}-po.patch
Patch1:		%{name}-desktop.patch
URL:		http://qballcow.nl/?name=gcursor&css=0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcursor is a little GTK+ program to change youre Xcursor with animated
preview. It sets a gconf key that is used by GNOME's session manager.
You need to log in GNOME again to make the changes.

%description -l pl
gcursor to ma³y, oparty na GTK+, program z animowanym podgl±dem, który
s³u¿y do zmiany kursora. Ustawia klucz gconf, który jest u¿ywany
przez zarz±dcê sesji GNOME. Aby zmiany zadzia³a³y, trzeba ponownie
zalogowaæ siê do GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
