Summary:	Additional modules for Asterisk
Name:		asterisk-addons
Version:	1.0.7
Release:	0.1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.digium.com/pub/asterisk/%{name}-%{version}.tar.gz
# Source0-md5:	4862b14d78cd1c4079a48c00d35696f9
URL:		http://www.asterisk.org/
BuildRequires:	asterisk-devel >= 1.0.0
BuildRequires:	mysql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional modules for Asterisk which are, for one reason or another,
not included in the normal base distribution. Many of these modules
are experimental.

%prep
%setup -q
sed -i -e s'#CFLAGS+=-I../asterisk#CFLAGS+=-I/usr/include/asterisk#g' Makefile

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
