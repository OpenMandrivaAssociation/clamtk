Summary:	Easy to use front-end for ClamAV

Name:		clamtk
Version:	5.18
Release:	2
License:	Artistic
Group:		File tools
URL:		https://github.com/dave-theunsub/%{name}/
Source0:	https://bitbucket.org/dave_theunsub/%{name}/downloads/%{name}-%{version}.tar.gz
Patch0:		%{name}-5.05-fix-UTF8-handling.patch
# Use more universal icon names to be able to run with both rosa-icons and oxygen
Patch1:         %{name}-5.05-icons.patch
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
Requires:	gettext
Requires:	perl(Gtk2) >= 1.241
Requires:	perl(Digest)
Requires:	perl(LWP)
Requires:	perl(JSON)
Requires:	perl(MIME::Base64)
Requires:	perl(Text::CSV)
Requires:	perl(File::Copy::Recursive)
Requires:	perl(Locale::gettext)
Requires:	perl(Time::Piece)
Requires:	clamav >= 0.98
Requires:	clamav-db
BuildArch:	noarch

%description
ClamTk is a GUI front-end for ClamAV using Gtk2-perl. It is designed to be an
easy-to-use, point and click virus scanner for Linux systems.


%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%doc CHANGES DISCLAIMER LICENSE README
%{_bindir}/%{name}
%{perl_vendorlib}/ClamTk
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
#{_datadir}/pixmaps/%%{name}-loader.gif
%{_mandir}/man1/%{name}.1.*


