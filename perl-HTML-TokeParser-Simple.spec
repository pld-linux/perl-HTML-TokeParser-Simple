#
# Conditional build:
%bcond_without tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	TokeParser-Simple
Summary:	HTML::TokeParser::Simple - easy to use HTML::TokeParser interface
Summary(pl):	HTML::TokeParser::Simple - ³atwy w u¿yciu interfejs do HTML::TokeParser
Name:		perl-HTML-TokeParser-Simple
Version:	2.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	65b1974178b129c8b0efd1d2dcd91efb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3.28
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::TokeParser is a fairly common method of parsing HTML. However,
the tokens returned are not exactly intuitive to parse.
HTML::TokeParser::Simple allows the user ask more intuitive (read:
more self-documenting) questions about the tokens returned.
Specifically, there are 7 is_foo type methods and 5 return_bar type
methods. The is_ methods allow you to determine the token type and the
return_ methods get the data that you need.

%description -l pl
HTML::TokeParser to dosyæ popularna metoda analizowania HTML-a. jednak
zwracane tokeny nie s± zbyt intuicyjne do przeanalizowania.
HTML::TokeParser::Simple pozwala wykonywaæ bardziej intuicyjne
(samodokumentuj±ce siê) zapytania dotycz±ce zwracanych tokenów. W
szczególno¶ci jest 7 metod typu is_foo oraz 5 metod typu return_bar.
Metody is_ pozwalaj± okre¶liæ typ tokenu, a metody return_ - pobraæ
potrzebne dane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/*
%{_mandir}/man3/*
