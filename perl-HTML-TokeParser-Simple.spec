#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	TokeParser-Simple
Summary:	HTML::TokeParser::Simple - easy to use HTML::TokeParser interface
Summary(pl.UTF-8):	HTML::TokeParser::Simple - łatwy w użyciu interfejs do HTML::TokeParser
Name:		perl-HTML-TokeParser-Simple
Version:	3.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f80b00fb71628caa02eeb86d729a6ed
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser >= 3.28
BuildRequires:	perl-Sub-Override
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

%description -l pl.UTF-8
HTML::TokeParser to dosyć popularna metoda analizowania HTML-a. jednak
zwracane tokeny nie są zbyt intuicyjne do przeanalizowania.
HTML::TokeParser::Simple pozwala wykonywać bardziej intuicyjne
(samodokumentujące się) zapytania dotyczące zwracanych tokenów. W
szczególności jest 7 metod typu is_foo oraz 5 metod typu return_bar.
Metody is_ pozwalają określić typ tokenu, a metody return_ - pobrać
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
