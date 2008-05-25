Summary:	Easy to use front-end for ClamAV
Name:		clamtk
Version:	3.09
Release:	%mkrel 1
License:	Artistic
Group:		File tools
URL:		http://clamtk.sourceforge.net/
Source:		http://downloads.sourceforge.net/clamtk/%{name}-%{version}.tar.bz2
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
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
install -D -m0644 clamtk.png %{buildroot}%{_datadir}/pixmaps/clamtk.png
install -D -m0644 clamtk.1.gz %{buildroot}%{_mandir}/man1/clamtk.1.gz
install -D -m0644 clamtk.desktop %{buildroot}%{_datadir}/applications/clamtk.desktop

for n in po/*.mo ; do
	%{__install} -D -m0644 $n %{buildroot}%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*

desktop-file-install \
	--add-category="GTK" \
	--add-category="Security" \
	--remove-category="Utility" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%post
%{update_menus}
%{update_desktop_database}
%{update_mime_database}

%postun
%{clean_menus}
%{clean_desktop_database}
%{clean_mime_database}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES DISCLAIMER LICENSE README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/clamtk.png
%{_mandir}/man1/%{name}.1.*
