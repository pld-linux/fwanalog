# TODO:
#	- missing files, missing requires
%define	pre	pre4
Summary:	firewall logfile analysis program
Summary(pl.UTF-8):	Analizator logów firewalla
Name:		fwanalog
Version:	0.6.4
Release:	0.%{pre}.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://tud.at/programm/fwanalog/%{name}-%{version}pre4.tar.gz
# Source0-md5:	6d54ec2aca8280be418640a937a5b5ef
URL:		http://tud.at/programm/fwanalog/
Requires:	analog
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fwanalog is a shell script that parses and summarizes firewall
logfiles. It currently (version 0.6.4pre4) understands logs from ipf
(tested with OpenBSD 2.8's and 2.9's ipf, also FreeBSD, NetBSD and
Solaris 8 with ipf), OpenBSD 3.x pf, Linux 2.2 ipchains, Linux 2.4
iptables, some ZyXEL/NetGear routers and (experimentally) Cisco PIX,
Watchguard Firebox and Firewall-One (not NG!) firewalls. It was tested
by author on Debian GNU/Linux "sid" with bash and OpenBSD 2.8, 2.9 and
3.x with ksh as /bin/sh. Other people use it on all kinds of Unix-like
platforms.

%description -l pl.UTF-8
fwanalog to skrypt powłoki przetwarzający i podsumowujący pliki logów
z firewalli. Aktualnie (w wersji 0.6.4pre4) rozumie logi z ipf
(testowane z ipf w OpenBSD 2.8 i 2.9, a także FreeBSD, NetBSD i
Solarisem 8 z ipf), pf z OpenBSD 3.x, ipchains z Linuksa 2.2, iptables
z Linuksa 2.4, niektórych routerów ZyXEL-a/NetGeara oraz
(eksperymentalnie) firewalli Cisco PIX, Watchguard Firebox oraz
Firewall-One (nie NG!). Skrypt był testowany przez autora na Debian
GNU/Linuksie "sid" z bashem oraz OpenBSD 2.8, 2.9 i 3.x z ksh jako
/bin/sh. Inni używali go na wszelkich rodzajach platform uniksowych.

%prep
%setup  -q -n %{name}-%{version}%{pre}

%install
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name}}

install fwanalog.sh $RPM_BUILD_ROOT%{_bindir}/fwanalog
install fwanalog.opts.linux24	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/fwanalog.opts
install services.conf fwanalog.analog.conf*	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CONTRIBUTORS README* TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/%{name}
