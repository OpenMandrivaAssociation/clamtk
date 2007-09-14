Summary:	Easy to use front-end for ClamAV
Name:		clamtk
Version:	3.03
Release:	%mkrel 1
License:	Artistic
Group:		File tools
URL:		http://clamtk.sourceforge.net/
Source:		http://dl.sf.net/clamtk/%{name}-%{version}.tar.bz2
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	gettext
Requires:	perl(Gtk2)
Requires:	perl(File::Find::Rule)
Requires:	perl(Date::Calc)
Requires:	perl(LWP)
Requires:	clamav >= 0.90 clamav-db gnomesu
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
ClamTk is a GUI front-end for ClamAV using Gtk2-perl.
It is designed to be an easy-to-use, point and click 
virus scanner for Linux systems.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -D -m0755 clamtk %{buildroot}%{_bindir}/clamtk
install -D -m0644 clamtk.xpm %{buildroot}%{_datadir}/pixmaps/clamtk.xpm
install -D -m0644 clamtk.1.gz %{buildroot}%{_mandir}/man1/clamtk.1.gz
install -D -m0644 clamtk.desktop %{buildroot}%{_datadir}/applications/clamtk.desktop

desktop-file-install \
  --remove-category="Utility" \
  --add-category="GTK" \
  --add-category="System;Security"\
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/%{name}.desktop

for n in po/*.mo ; do
	%{__install} -D -m0644 $n %{buildroot}%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

%find_lang %{name}

%define nameicon clamtk.xpm

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -scale 48x48 %{nameicon} %{buildroot}/%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32x32 %{nameicon} %{buildroot}/%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16x16 %{nameicon} %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%post
%{update_menus}
%{update_desktop_database}
%{update_mime_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%{clean_mime_database}
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES DISCLAIMER LICENSE README
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/clamtk.xpm
%{_mandir}/man1/%{name}.1.*
