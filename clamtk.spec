Summary:	Easy to use front-end for ClamAV

Name:		clamtk
Version:	6.07
Release:	1
License:	Artistic
Group:		File tools
URL:		https://gitlab.com/dave_m/clamtk/
Source0:	https://bitbucket.org/davem_/clamtk-gtk3/downloads/%{name}-%{version}.tar.xz
Patch0:		%{name}-5.05-fix-UTF8-handling.patch
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
Requires:	gettext
Requires:	perl(File::Find::Rule)
Requires:	perl(Date::Calc)
Requires:	perl(LWP)
Requires:	clamav >= 0.98
Requires:	clamav-db
Recommends:	yelp
BuildArch:	noarch

%description
ClamTk is a GUI front-end for ClamAV using Gtk2-perl. It is designed to be an
easy-to-use, point and click virus scanner for Linux systems.


%prep
%setup -q
%patch0 -p1

%build
# Nothing to do

%install
%{__install} -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
%{__install} -D -m0644 images/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{__install} -D -m0644 images/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
#{__install} -D -m0644 images/%%{name}-loader.gif %%{buildroot}%%{_datadir}/pixmaps/%%{name}-loader.gif
%{__install} -D -m0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz
%{__install} -D -m0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__install} -d %{buildroot}%{perl_vendorlib}/ClamTk
%{__install} -m0644 lib/*.pm %{buildroot}%{perl_vendorlib}/ClamTk

for n in po/*.mo ; do
	%{__install} -D -m0644 $n %{buildroot}%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/%{name}.mo
done

desktop-file-install \
	--add-category="System" \
	--remove-category="Security" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}


%files -f %{name}.lang
%doc CHANGES DISCLAIMER LICENSE README.md
%{_bindir}/%{name}
%{perl_vendorlib}/ClamTk
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
#{_datadir}/pixmaps/%%{name}-loader.gif
%{_mandir}/man1/%{name}.1.*


