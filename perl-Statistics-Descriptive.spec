%define modname	Statistics-Descriptive
%define modver 3.0607

Summary:	Module of basic descriptive statistical functions
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Statistics/Statistics-Descriptive-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildRequires: perl(List::MoreUtils)

%description
This module provides basic functions used in descriptive statistics. It has an
object oriented design and supports two different types of data storage and
calculation objects:	sparse and full. With the sparse method, none of the data
is stored and only a few statistical measures are available. Using the full
method, the entire data set is retained and additional functions are available.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/Statistics
%{_mandir}/man3/*



