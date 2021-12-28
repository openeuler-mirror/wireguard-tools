Name:           wireguard-tools
Version:        1.0.20210424
Release:        1
URL:            https://www.wireguard.com/
Summary:        Fast, modern, secure VPN tunnel
License:        GPLv2

Source0:        https://git.zx2c4.com/%{name}/snapshot/%{name}-%{version}.tar.xz

%{?systemd_requires}
BuildRequires: make
BuildRequires: systemd
BuildRequires: gcc

%description
WireGuard is a novel VPN that runs inside the Linux Kernel and uses
state-of-the-art cryptography (the "Noise" protocol). It aims to be
faster, simpler, leaner, and more useful than IPSec, while avoiding
the massive headache. It intends to be considerably more performant
than OpenVPN. WireGuard is designed as a general purpose VPN for
running on embedded interfaces and super computers alike, fit for
many different circumstances. It runs over UDP.

This package provides the wg binary for controlling WireGuard.

%prep
%autosetup -p1

%build
%set_build_flags

## Start DNS Hatchet
pushd contrib/dns-hatchet
./apply.sh
popd
## End DNS Hatchet

%make_build RUNSTATEDIR=%{_rundir} -C src

%install
%make_install BINDIR=%{_bindir} MANDIR=%{_mandir} RUNSTATEDIR=%{_rundir} \
WITH_BASHCOMPLETION=yes WITH_WGQUICK=yes WITH_SYSTEMDUNITS=yes -C src

%files
%doc README.md contrib
%license COPYING
%{_bindir}/wg
%{_bindir}/wg-quick
%{_sysconfdir}/wireguard/
%{_datadir}/bash-completion/completions/wg
%{_datadir}/bash-completion/completions/wg-quick
%{_unitdir}/wg-quick@.service
%{_unitdir}/wg-quick.target
%{_mandir}/man8/wg.8*
%{_mandir}/man8/wg-quick.8*

%changelog
* Mon Dec 27 2021 duyiwei <duyiwei@kylinos.cn> - 1.0.20210424-1
- Package init
