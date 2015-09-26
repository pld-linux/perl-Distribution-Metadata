#
# Conditional build:
%bcond_with	tests		# do not perform "make test"

%define		pdir	Distribution
%define		pnam	Metadata
%include	/usr/lib/rpm/macros.perl
Summary:	Distribution::Metadata - gather distribution metadata in local
Name:		perl-Distribution-Metadata
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SK/SKAJI/Distribution-Metadata-%{version}.tar.gz
# Source0-md5:	eda72550f45b67cc3257012618fd8923
URL:		http://search.cpan.org/dist/Distribution-Metadata/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CPAN-DistnameInfo
BuildRequires:	perl-File-pushd
BuildRequires:	perl-JSON
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Distribution::Metadata gathers distribution metadata in local.

Please note that as mentioned above, this module deeply depends on
cpanm behavior. If you install cpan modules by hands or some cpan
clients other than cpanm, this module won't work.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/which-meta
%{perl_vendorlib}/Distribution/*.pm
%{perl_vendorlib}/Distribution/Metadata
%{_mandir}/man1/which-meta.1p*
%{_mandir}/man3/Distribution::Metadata.3pm*
%{_mandir}/man3/Distribution::Metadata::Factory.3pm*
