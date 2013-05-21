%define upstream_name    Statistics-Descriptive
%define upstream_version 3.0201

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Module of basic descriptive statistical functions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Statistics/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildArch: noarch

%description
This module provides basic functions used in descriptive statistics. It has an
object oriented design and supports two different types of data storage and
calculation objects: sparse and full. With the sparse method, none of the data
is stored and only a few statistical measures are available. Using the full
method, the entire data set is retained and additional functions are available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/Statistics
%{_mandir}/*/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.20.100-4mdv2012.0
+ Revision: 765653
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.20.100-3
+ Revision: 764165
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 3.20.100-2
+ Revision: 676910
- rebuild

* Fri Nov 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.20.100-1mdv2011.0
+ Revision: 596649
- update to 3.0201

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 3.20.0-1mdv2011.0
+ Revision: 551199
- update to 3.0200

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 3.10.0-1mdv2010.0
+ Revision: 398939
- update to 3.0100
- using %%perl_convert_version
- fixed license field

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.0000-1mdv2010.0
+ Revision: 383542
- update to new version 3.0000

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 2.9-1mdv2010.0
+ Revision: 376141
- update to new version 2.9

* Sun May 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.8-1mdv2010.0
+ Revision: 373930
- update to new version 2.8

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.7-1mdv2010.0
+ Revision: 371794
- update to new version 2.7

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.6-10mdv2009.0
+ Revision: 258384
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.6-9mdv2009.0
+ Revision: 246453
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2.6-7mdv2008.1
+ Revision: 136347
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.6-7mdv2008.0
+ Revision: 86910
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.6-6mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.6-5mdk
- spec cleanup
- better URL
- %%mkrel

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.6-4mdk
- fix buildrequires in a backward compatible way

* Wed Aug 04 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.6-3mdk
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.6-2mdk
- fixed dir ownership (distlint)

* Mon Jan 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.6-1mdk
- first mdk release

