# TODO: optflags, files
Summary:	Additional modules for Asterisk
Summary(pl):	Dodatkowe modu³y dla Asteriska
Name:		asterisk-addons
Version:	1.2.1
Release:	0.1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.digium.com/pub/asterisk/%{name}-%{version}.tar.gz
# Source0-md5:	4862b14d78cd1c4079a48c00d35696f9
URL:		http://www.asterisk.org/
BuildRequires:	asterisk-devel >= 1.0.0
BuildRequires:	mysql-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional modules for Asterisk which are, for one reason or another,
not included in the normal base distribution. Many of these modules
are experimental.

%description -l pl
Dodatkowe modu³y dla Asteriska, które z ró¿nych powodów nie zosta³y
w³±czone do g³ównej dystrybucji. Wiele z tych modu³ów jest
eksperymentalnych.

%prep
%setup -q
#sed -i -e s'#CFLAGS+=-I../asterisk#CFLAGS+=-I/usr/include/asterisk#g' Makefile

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/%{_libdir}/asterisk/modules,/%{_sysconfdir}/asterisk}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install configs/cdr_mysql.conf.sample $RPM_BUILD_ROOT/%{_sysconfdir}/asterisk/cdr_mysql.conf
install configs/res_mysql.conf.sample $RPM_BUILD_ROOT/%{_sysconfdir}/asterisk/res_mysql.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/cdr_mysql.txt
%dir %{_sysconfdir}/asterisk
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/*.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/*.so
