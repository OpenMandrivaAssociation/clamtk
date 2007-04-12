%define section	System/File Tools	
%define version 2.31
%define release 1

Summary: 	Easy to use front-end for ClamAV
Name: 		clamtk
Version: 	%version
Release: 	%mkrel %release
License: 	Artistic
Group: 		File tools
URL: 		http://clamtk.sourceforge.net/
Source: 	http://dl.sf.net/clamtk/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  perl-Gtk2 perl-File-Find-Rule perl-Date-Calc perl-libwww-perl
BuildRequires:	desktop-file-utils ImageMagick perl-encoding-warnings
Requires: 	perl-Gtk2 perl-File-Find-Rule perl-Date-Calc perl-libwww-perl
Requires: 	clamav >= 0.83 clamav-db gnomesu
BuildArch: 	noarch

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
ClamTk is a GUI front-end for ClamAV using Gtk2-perl.
It is designed to be an easy-to-use, point and click 
virus scanner for Linux systems.

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 clamtk %{buildroot}%{_bindir}/clamtk
%{__install} -D -m0644 clamtk.xpm %{buildroot}%{_datadir}/pixmaps/clamtk.xpm
%{__install} -D -m0644 clamtk.1.gz %{buildroot}%{_mandir}/man1/clamtk.1.gz
%{__install} -D -m0644 clamtk.desktop %{buildroot}%{_datadir}/applications/clamtk.desktop

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --add-category="System;Security"\
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop

%{__mkdir} -p %{buildroot}%{_datadir}/locale/{da,de,fr,it,pt_BR,ru,zh_CN}/LC_MESSAGES

for n in po/*.mo ; do
	%{__install} -D -m0644 $n %{buildroot}%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

%find_lang %name

%define  nameicon clamtk.xpm

mkdir -p %{buildroot}{%_liconsdir,%_iconsdir,%_miconsdir}
convert -scale 48x48 %{nameicon} %{buildroot}/%{_liconsdir}/%{name}.png
convert -scale 32x32 %{nameicon} %{buildroot}/%{_iconsdir}/%{name}.png
convert -scale 16x16 %{nameicon} %{buildroot}/%{_miconsdir}/%{name}.png

%post
%{update_desktop_database}
%{update_mime_database}

%postun
%{clean_desktop_database}
%{clean_mime_database}

%clean
%{__rm} -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc CHANGES DISCLAIMER LICENSE README
%{_bindir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/clamtk.xpm
%{_mandir}/man1/%name.1.bz2


