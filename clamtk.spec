Summary:	Easy to use front-end for ClamAV
Name:		clamtk
Version:	4.45
Release:	3
License:	Artistic
Group:		File tools
URL:		http://clamtk.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/ClamTk/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
#Requires:	perl(Gtk2)
Requires:	perl(File::Find::Rule)
#Requires:	perl(Date::Calc)
Requires:	perl(LWP)
Requires:	clamav >= 0.95
Requires:	clamav-db
Requires(post,postun):	desktop-file-utils
BuildArch:	noarch

%description
ClamTk is a GUI front-end for ClamAV using Gtk2-perl. It is designed to be an
easy-to-use, point and click virus scanner for Linux systems.

%prep
%setup -q

%build

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0644 images/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m0644 images/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
install -D -m0644 images/%{name}-loader.gif %{buildroot}%{_datadir}/pixmaps/%{name}-loader.gif
install -D -m0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz
install -D -m0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -d %{buildroot}%{perl_vendorlib}/ClamTk
install -m0644 lib/*.pm %{buildroot}%{perl_vendorlib}/ClamTk

for n in po/*.mo ; do
	%{__install} -D -m0644 $n %{buildroot}%{_datadir}/locale/`basename $n .mo`/LC_MESSAGES/%{name}.mo
done

desktop-file-install \
	--add-category="System" \
	--remove-category="Utility" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc CHANGES DISCLAIMER LICENSE README
%{_bindir}/%{name}
%{perl_vendorlib}/ClamTk
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/pixmaps/%{name}-loader.gif
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri May 31 2013 Giovanni Mariani <mc2374@mclink.it> 4.45-1
- New release 4.45

* Wed Jan 09 2013 Giovanni Mariani <mc2374@mclink.it> 4.44-1
- New release 4.44
- Removed a couple of explicit Reqs (alredy added implicitly by the
  building process) and silenced build warnings
- Bumped Req for clamav to a more recent one
- Installed more image files (.xpm and .gif)
- Dropped useless things in .desktop file processing (GTK category is already
  present; mimetype=xxx is no more present

* Thu Aug 16 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.41-1
+ Revision: 814954
- update to new version 4.41
- spec file clean

* Sun Feb 19 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 4.37-1
+ Revision: 777410
- update to new version 4.37
- fix find_lang macro

* Thu Oct 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.36-1
+ Revision: 707437
- update to new version 4.36

* Mon Oct 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.35-1
+ Revision: 704040
- update to new version 4.35

* Thu Aug 18 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.34-1
+ Revision: 695248
- update to new version 4.34

* Tue Jun 14 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.33-1
+ Revision: 685166
- update to new version 4.33

* Sat May 07 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.32-1
+ Revision: 672198
- update to new version 4.32

* Wed Jan 26 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 4.31-1
+ Revision: 632809
- update to new version 4.31

* Sat Nov 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.30-1mdv2011.0
+ Revision: 601905
- update to new version 4.30

* Sun Oct 03 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.29-1mdv2011.0
+ Revision: 582706
- update to new version 4.29

* Wed Aug 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.28-1mdv2011.0
+ Revision: 571225
- update to new version 4.28

* Sun Jul 11 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.27-1mdv2011.0
+ Revision: 550915
- update to new version 4.27

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 4.26-1mdv2010.1
+ Revision: 543255
- update to new version 4.26

* Sun Mar 28 2010 Ahmad Samir <ahmadsamir@mandriva.org> 4.25-2mdv2010.1
+ Revision: 528299
- fix .desktop file

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.25-1mdv2010.1
+ Revision: 516292
- update to 4.25

* Mon Mar 01 2010 Frederik Himpe <fhimpe@mandriva.org> 4.24-1mdv2010.1
+ Revision: 513065
- update to new version 4.24

* Wed Jan 20 2010 Frederik Himpe <fhimpe@mandriva.org> 4.23-1mdv2010.1
+ Revision: 494125
- update to new version 4.23

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 4.22-1mdv2010.1
+ Revision: 482695
- update to new version 4.22

* Sun Dec 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.21-1mdv2010.1
+ Revision: 474133
- update to new version 4.21
- correct url for Source0

* Wed Nov 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.20-2mdv2010.1
+ Revision: 464846
- fix installation directory (mdvbz #54792)

* Sat Nov 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.20-1mdv2010.1
+ Revision: 462261
- update to new version 4.20

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 4.18-1mdv2010.0
+ Revision: 444861
- update to new version 4.18

* Sat Aug 08 2009 Frederik Himpe <fhimpe@mandriva.org> 4.17-1mdv2010.0
+ Revision: 411799
- update to new version 4.17

* Sat Jul 11 2009 Frederik Himpe <fhimpe@mandriva.org> 4.16-1mdv2010.0
+ Revision: 394896
- update to new version 4.16

* Sun Jun 21 2009 Frederik Himpe <fhimpe@mandriva.org> 4.15-1mdv2010.0
+ Revision: 387568
- update to new version 4.15

* Sat Jun 13 2009 Frederik Himpe <fhimpe@mandriva.org> 4.14-1mdv2010.0
+ Revision: 385755
- update to new version 4.14

* Tue May 26 2009 Frederik Himpe <fhimpe@mandriva.org> 4.13-1mdv2010.0
+ Revision: 379969
- update to new version 4.13

* Fri May 01 2009 Frederik Himpe <fhimpe@mandriva.org> 4.12-1mdv2010.0
+ Revision: 369684
- update to new version 4.12

* Sun Mar 22 2009 Frederik Himpe <fhimpe@mandriva.org> 4.11-1mdv2009.1
+ Revision: 360405
- update to new version 4.11

* Wed Feb 18 2009 Frederik Himpe <fhimpe@mandriva.org> 4.10-1mdv2009.1
+ Revision: 342617
- Update to new version 4.10

* Sun Feb 15 2009 Funda Wang <fwang@mandriva.org> 4.09-1mdv2009.1
+ Revision: 340610
- New version 4.09

* Sun Dec 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.08-1mdv2009.1
+ Revision: 320421
- update to new version 4.08

* Sat Dec 20 2008 Funda Wang <fwang@mandriva.org> 4.07-1mdv2009.1
+ Revision: 316480
- update to new version 4.07

* Sun Dec 07 2008 Funda Wang <fwang@mandriva.org> 4.06-1mdv2009.1
+ Revision: 311636
- new version 4.06

* Fri Nov 28 2008 Funda Wang <fwang@mandriva.org> 4.05-1mdv2009.1
+ Revision: 307455
- update to new version 4.05

* Sun Nov 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.04-1mdv2009.1
+ Revision: 303833
- update to new version 4.04

* Tue Nov 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.03-1mdv2009.1
+ Revision: 302115
- update to new version 4.03

* Mon Oct 27 2008 Funda Wang <fwang@mandriva.org> 4.02-2mdv2009.1
+ Revision: 297525
- install pm files
- update to new version 4.02

* Mon Oct 20 2008 Funda Wang <fwang@mandriva.org> 4.01-1mdv2009.1
+ Revision: 295472
- New version 4.01

* Mon Oct 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 4.00-1mdv2009.1
+ Revision: 293414
- update to new version 4.00

* Thu Aug 28 2008 Funda Wang <fwang@mandriva.org> 3.11-1mdv2009.0
+ Revision: 276771
- update to new version 3.11

* Sun Jun 15 2008 Funda Wang <fwang@mandriva.org> 3.10-1mdv2009.0
+ Revision: 219268
- update to new version 3.10

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun May 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.09-1mdv2009.0
+ Revision: 211216
- update to new version 3.09

* Wed Feb 06 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.08-1mdv2008.1
+ Revision: 162906
- new version

* Sun Jan 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 3.07-1mdv
+ Revision: 155286
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.06-1mdv2008.1
+ Revision: 139734
- drop patch 0, use desktop-file-utils instead of
- move icon to pixmap dir
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 16 2007 Funda Wang <fwang@mandriva.org> 3.05-1mdv2008.1
+ Revision: 120548
- New version 3.05

* Wed Oct 10 2007 Jérôme Soyer <saispo@mandriva.org> 3.04-1mdv2008.1
+ Revision: 96789
- Add .desktop file
- Fix .desktop
- Add files
- New release 3.04

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version

* Fri Aug 31 2007 Funda Wang <fwang@mandriva.org> 3.01-1mdv2008.0
+ Revision: 77152
- Drop useless BR
- New version 3.01

* Thu Aug 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.00-1mdv2008.0
+ Revision: 60953
- new version

* Mon Jun 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.99-1mdv2008.0
+ Revision: 44096
- vew version
- drop X-MandrivaLinux
- move icons to the fd.o compiliant directory
- add scriplets
- spec file clean

* Fri May 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.32-1mdv2008.0
+ Revision: 27748
- new version


* Sun Apr 01 2007 Jérôme Soyer <saispo@mandriva.org> 2.31-1mdv2007.1
+ Revision: 150140
- New release

* Mon Mar 12 2007 Jérôme Soyer <saispo@mandriva.org> 2.30-1mdv2007.1
+ Revision: 141673
- New release 2.30

* Tue Mar 06 2007 Jérôme Soyer <saispo@mandriva.org> 2.29-1mdv2007.1
+ Revision: 133565
- New release 2.29

* Sun Mar 04 2007 Jérôme Soyer <saispo@mandriva.org> 2.28-2mdv2007.1
+ Revision: 132601
- Rebuild for new clamav

* Wed Feb 28 2007 Jérôme Soyer <saispo@mandriva.org> 2.28-1mdv2007.1
+ Revision: 126948
- New release 2.28

* Thu Jan 18 2007 Jérôme Soyer <saispo@mandriva.org> 2.27-1mdv2007.1
+ Revision: 110179
- New release 2.27

* Mon Nov 27 2006 Jérôme Soyer <saispo@mandriva.org> 2.26-1mdv2007.1
+ Revision: 87476
- Add BuildRequires
- Add BuildRequires
- New release 2.26
- New release 2.24
- Import clamtk

* Mon Sep 04 2006 Jerome Soyer <saispo@mandriva.org> 2.23-3mdv2007.0
- Fix run menu

* Sun Sep 03 2006 Jerome Soyer <saispo@mandriva.rog> 2.23-2mdv2007.0
- Update .desktop
- Using Multilang

* Wed Aug 30 2006 Jerome Soyer <saispo@mandriva.org> 2.23-1mdv2007.0
- New release 2.23

* Mon Jul 31 2006 Jerome Soyer <saispo@mandriva.org> 2.22-1mdv2007.0
- New release 2.22

* Sun Jul 16 2006 Jerome Soyer <saispo@mandriva.org> 2.21-1mdv2007.0
- New release 2.21

* Thu Jun 22 2006 Jerome Soyer <saispo@mandriva.org> 2.20-1mdv2007.0
- New release 2.20
- XDG Menu Entry

* Wed May 17 2006 Jerome Soyer <saispo@mandriva.org> 2.19-1mdk
- New release 2.19

* Mon May 08 2006 Jerome Soyer <saispo@mandriva.org> 2.18-1mdk
- New release 2.18

* Mon Apr 24 2006 Jerome Soyer <saispo@mandriva.org> 2.17-1mdk
- New release 2.17

* Fri Apr 07 2006 Jerome Soyer <saispo@mandriva.org> 2.16-1mdk
- New release 2.16

* Thu Apr 06 2006 Jerome Soyer <saispo@mandriva.org> 2.15-1mdk
- First, thks to Steffen Van Roosbroeck for the initial spec
- rpmbuildupdate aware

