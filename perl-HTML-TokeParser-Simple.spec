
# Conditional build:
%bcond_without tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	TokeParser-Simple
Summary:	Easy to use HTML::TokeParser interface
Summary(pl):	£atwy w u¿yciu interfejs do HTML::TokeParser
Name:		perl-HTML-TokeParser-Simple
Version:	2.1
Release:	1
License:	Same as Perl itself
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d93cdfa3f816664d35a20d8bff579dca
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{perl_vendorlib}/%{pdir}
%{_mandir}/man3/*
