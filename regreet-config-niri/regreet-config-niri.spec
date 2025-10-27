Name:           regreet-config-niri
Version:        1
Release:        0%{?dist}
Summary:        regreet config for niri
License:        GPL-3.0-or-later
BuildArch:      noarch
Source1:        config.toml
Source2:        regreet-config-niri.kdl
Requires:       regreet niri

%description
%{summary}

%install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/greetd/config.toml
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/greetd/regreet-config-niri.kdl

%files
%dir %{_sysconfdir}/greetd
%config(noreplace) %{_sysconfdir}/greetd/config.toml
%config(noreplace) %{_sysconfdir}/greetd/regreet-config-niri.kdl

%changelog
%autochangelog
