# TODO:		optflags
Summary:	Additional modules for Asterisk
Summary(pl.UTF-8):	Dodatkowe moduły dla Asteriska
Name:		asterisk-addons
Version:	1.4.1
Release:	1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.digium.com/pub/asterisk/%{name}-%{version}.tar.gz
# Source0-md5:	e776b23eac9552e3543fba9202dd7c7d
URL:		http://www.asterisk.org/
BuildRequires:	asterisk-devel >= 1.4.0
BuildRequires:	mysql-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional modules for Asterisk which are, for one reason or another,
not included in the normal base distribution. Many of these modules
are experimental.

%description -l pl.UTF-8
Dodatkowe moduły dla Asteriska, które z różnych powodów nie zostały
włączone do głównej dystrybucji. Wiele z tych modułów jest
eksperymentalnych.

%prep
%setup -q
sed -i -e "s#/usr/lib/#/usr/%{_lib}/#g#" Makefile asterisk-ooh323c/Makefile.in

%build
%configure
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir}/asterisk/modules,%{_sysconfdir}/asterisk}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALLTO=$RPM_BUILD_ROOT%{_libdir}/asterisk/modules

install configs/cdr_mysql.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/asterisk/cdr_mysql.conf
install configs/res_mysql.conf.sample $RPM_BUILD_ROOT%{_sysconfdir}/asterisk/res_mysql.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/cdr_mysql.txt
%dir %{_sysconfdir}/asterisk
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/*.conf
%dir %{_libdir}/asterisk
%dir %{_libdir}/asterisk/modules
%attr(755,root,root) %{_libdir}/asterisk/modules/*.so
