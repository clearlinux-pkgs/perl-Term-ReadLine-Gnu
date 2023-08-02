#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Term-ReadLine-Gnu
Version  : 1.46
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-1.46.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-1.46.tar.gz
Summary  : 'Perl extension for the GNU Readline/History Library'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Term-ReadLine-Gnu-bin = %{version}-%{release}
Requires: perl-Term-ReadLine-Gnu-man = %{version}-%{release}
Requires: perl-Term-ReadLine-Gnu-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : pkgconfig(ncurses)
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory is for filename completion test.
The size of most of files in this directory is zero.

%package bin
Summary: bin components for the perl-Term-ReadLine-Gnu package.
Group: Binaries

%description bin
bin components for the perl-Term-ReadLine-Gnu package.


%package dev
Summary: dev components for the perl-Term-ReadLine-Gnu package.
Group: Development
Requires: perl-Term-ReadLine-Gnu-bin = %{version}-%{release}
Provides: perl-Term-ReadLine-Gnu-devel = %{version}-%{release}
Requires: perl-Term-ReadLine-Gnu = %{version}-%{release}

%description dev
dev components for the perl-Term-ReadLine-Gnu package.


%package man
Summary: man components for the perl-Term-ReadLine-Gnu package.
Group: Default

%description man
man components for the perl-Term-ReadLine-Gnu package.


%package perl
Summary: perl components for the perl-Term-ReadLine-Gnu package.
Group: Default
Requires: perl-Term-ReadLine-Gnu = %{version}-%{release}

%description perl
perl components for the perl-Term-ReadLine-Gnu package.


%prep
%setup -q -n Term-ReadLine-Gnu-1.46
cd %{_builddir}/Term-ReadLine-Gnu-1.46

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/perlsh

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Term::ReadLine::Gnu.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/perlsh.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
