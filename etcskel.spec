Summary:	Mandriva Linux default files for new users' home directories
Name:		etcskel
Version:	1.63
Release:	31
License:	Public Domain
Group:		System/Base
# get the source from our cvs repository (see
# http://cvs.mandriva.com)
Source0:	%{name}-%{version}.tar.bz2
Source1:	etcskel.rpmlintrc
Requires:	bash
BuildArch:	noarch

%description
The etcskel package is part of the basic Mandriva system.

Etcskel provides the /etc/skel directory's files. These files are then placed
in every new user's home directory when new accounts are created.

%prep
%setup -q

%install

%makeinstall_std

%files
%defattr(-,root,root)
%doc ChangeLog
%config(noreplace) /etc/skel



%changelog
* Mon Jun 20 2011 Alex Burmashev <burmashev@mandriva.org> 1.63-29mdv2011.0
+ Revision: 686100
- removed tmp directory from /home/burmashev/

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.63-28
+ Revision: 664151
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.63-27mdv2011.0
+ Revision: 605106
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.63-26mdv2010.1
+ Revision: 522575
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.63-25mdv2010.0
+ Revision: 424389
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.63-24mdv2009.1
+ Revision: 350981
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.63-23mdv2009.0
+ Revision: 220728
- rebuild
- fix URL

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.63-22mdv2008.1
+ Revision: 149700
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.63-21mdv2008.0
+ Revision: 90165
- rebuild for 2008


* Tue Feb 27 2007 Olivier Blin <oblin@mandriva.com> 1.63-20mdv2007.0
+ Revision: 126444
- do not make rpm override /etc/skel/tmp permissions (#28952)
- spec cleanups

* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.63-19mdv2007.1
+ Revision: 119953
- Import etcskel

* Fri Oct 21 2005 Olivier Thauvin <nanardon@mandriva.org> 1.63-18mdk
- s/Mandrake/Mandriva/
- rebuild
- spec cleanup
- apply upstream change of 16mdk

* Fri Aug 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.63-17mdk
- 1.63-16mdk was corrupted

* Thu Aug 26 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.63-16mdk
- removed obsolete /etc/skel/.mailcap with wvHtml entry for
  application/msword mime type.

