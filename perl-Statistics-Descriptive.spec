%define module  Statistics-Descriptive
%define name    perl-%{module}
%define version 2.6
%define release %mkrel 7

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Module of basic descriptive statistical functions
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Statistics/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides basic functions used in descriptive statistics. It has an
object oriented design and supports two different types of data storage and
calculation objects: sparse and full. With the sparse method, none of the data
is stored and only a few statistical measures are available. Using the full
method, the entire data set is retained and additional functions are available.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Statistics
%{_mandir}/*/*

