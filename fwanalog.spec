%define	pre	pre4
Summary:	firewall logfile analysis program
Summary(pl):	Analizator logów firewalla
Name:		fwanalog
Version:	0.6.4
Release:	0.%{pre}.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://tud.at/programm/fwanalog/%{name}-%{version}pre4.tar.gz
# Source0-md5:	6d54ec2aca8280be418640a937a5b5ef
URL:		http://tud.at/programm/fwanalog/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wanalog is a shell script that parses and summarizes firewall
logfiles. It currently (version 0.6.4pre4) understands logs from ipf
(tested with OpenBSD 2.8's and 2.9's ipf, also FreeBSD, NetBSD and
Solaris 8 with ipf), OpenBSD 3.x pf, Linux 2.2 ipchains, Linux 2.4
iptables, some ZyXEL/NetGear routers and (experimentally) Cisco PIX,
Watchguard Firebox and Firewall-One (not NG!) firewalls. I have tested
it on Debian GNU/Linux "sid" with bash and OpenBSD 2.8, 2.9 and 3.x
with ksh as /bin/sh. Other people use it on all kinds of Unix-like
platforms.

%prep
%setup  -q -n %{name}-%{version}%{pre}

%build

%install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
