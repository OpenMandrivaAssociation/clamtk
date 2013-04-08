Summary:	Easy to use front-end for ClamAV
Name:		clamtk
Version:	4.42
Release:	2
License:	Artistic
Group:		File tools
Url:		http://clamtk.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/clamtk/ClamTk/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	gettext
BuildRequires:	desktop-file-utils
Requires:	perl(Gtk2)
Requires:	perl(File::Find::Rule)
Requires:	perl(Date::Calc)
Requires:	perl(LWP)
Requires:	clamav >= 0.90
Requires:	clamav-db
Requires:	gnomesu
Requires(post,postun):	desktop-file-utils

%description
ClamTk is a GUI front-end for ClamAV using Gtk2-perl.
It is designed to be an easy-to-use, point and click
virus scanner for Linux systems.

%prep
%setup -q

%build

%install
install -D -m0755 clamtk %{buildroot}%{_bindir}/clamtk
install -D -m0644 images/clamtk.png %{buildroot}%{_datadir}/pixmaps/clamtk.png
install -D -m0644 clamtk.1.gz %{buildroot}%{_mandir}/man1/clamtk.1.gz
install -D -m0644 clamtk.desktop %{buildroot}%{_datadir}/applications/clamtk.desktop
install -d %{buildroot}%{perl_vendorlib}/ClamTk
install -m0644 lib/*.pm %{buildroot}%{perl_vendorlib}/ClamTk

for n in po/*.mo ; do
	install -D -m0644 $n %{buildroot}%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/clamtk.mo
done

desktop-file-install \
	--add-category="GTK" \
	--remove-category="Security" \
	--remove-mime-type="vms/exe" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc CHANGES DISCLAIMER LICENSE README
%{_bindir}/%{name}
%{perl_vendorlib}/ClamTk
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/clamtk.png
%{_mandir}/man1/%{name}.1.*

