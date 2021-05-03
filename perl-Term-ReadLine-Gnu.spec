#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Term-ReadLine-Gnu
Version  : 1.41
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-1.41.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/Term-ReadLine-Gnu-1.41.tar.gz
Summary  : 'Perl extension for the GNU Readline/History Library'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Term-ReadLine-Gnu-bin = %{version}-%{release}
Requires: perl-Term-ReadLine-Gnu-man = %{version}-%{release}
Requires: perl-Term-ReadLine-Gnu-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : pkgconfig(ncurses)
BuildRequires : readline-dev

%description
Term::ReadLine::Gnu --- GNU Readline Library Wrapper Module
This program is free software; you can redistribute it and/or
modify it under the same terms as Perl itself.

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
%setup -q -n Term-ReadLine-Gnu-1.41
cd %{_builddir}/Term-ReadLine-Gnu-1.41

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/Term/ReadLine/Gnu.pm
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/Term/ReadLine/Gnu/XS.pm
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/Gnu.so
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/Tk_getc.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/_ch_wrapper.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/_str2fn.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/_str2map.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/_tgetstrs.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/_trp_completion_function.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/autosplit.ix
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/change_ornaments.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/display_readline_version.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/get_history_event.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/hist_arg_extract.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/hist_list.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/history_expand_line.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/list_completion_function.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/operate_and_get_next.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/ornaments.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_add_funmap_entry.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_bind_key.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_bind_key_if_unbound.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_bind_keyseq.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_bind_keyseq_if_unbound.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_call_function.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_completion_mode.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_copy_keymap.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_discard_keymap.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_filename_list.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_generic_bind.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_invoking_keyseqs.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_macro_bind.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_message.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_set_key.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_set_keymap.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_tty_set_default_bindings.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/rl_tty_unset_default_bindings.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/shadow_redisplay.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/unbind_command.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/unbind_function.al
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Term/ReadLine/Gnu/XS/unbind_key.al
