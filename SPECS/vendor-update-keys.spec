Summary: Public keys for third-party updates
Name: vendor-update-keys
Version: 1.3.6
Release: 1.2%{?dist}
URL: https://github.com/xcp-ng-rpms/vendor-update-keys
Source0: RPM-GPG-KEY-AMD-MXGPU
Source1: RPM-GPG-KEY-BITDEFENDER
Source2: RPM-GPG-KEY-DELL
Source3: RPM-GPG-KEY-FUJITSU
Source4: RPM-GPG-KEY-HPE
Source5: RPM-GPG-KEY-NVIDIA
Source6: RPM-GPG-KEY-QLGC
Source7: RPM-GPG-KEY-VATES-SA
Source8: RPM-GPG-KEY-XS-OPENSTACK
License: GPG Public Keys

BuildArch: noarch

%description
Public keys used by vendors to sign supplemental packs.

%install
install -m 0755 -d %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE0} %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE1} %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE2} %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE3} %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE4} %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE5} %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE6} %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE7} %{buildroot}/etc/firstboot.d/data/keys/
install -m 0644 %{SOURCE8} %{buildroot}/etc/firstboot.d/data/keys/

%files
/etc/firstboot.d/data/keys/*

%changelog
* Mon Apr 29 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.3.6-1.2
- Rebuild for XCP-ng 8.0

* Thu Jan 24 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.3.6-1.1
- Initial package for XCP-ng.

