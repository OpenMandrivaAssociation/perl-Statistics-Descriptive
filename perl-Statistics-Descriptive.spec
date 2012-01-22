%define upstream_name    Statistics-Descriptive
%define upstream_version 3.0201

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 4

Summary:        Module of basic descriptive statistical functions
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Statistics/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Buildarch: noarch

%description
This module provides basic functions used in descriptive statistics. It has an
object oriented design and supports two different types of data storage and
calculation objects: sparse and full. With the sparse method, none of the data
is stored and only a few statistical measures are available. Using the full
method, the entire data set is retained and additional functions are available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

