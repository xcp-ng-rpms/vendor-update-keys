Summary: Public keys for third-party updates
Name: vendor-update-keys
Version: 1.3.7
Release: 1.3%{?dist}
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
Source9: RPM-GPG-KEY-BRCM-ECD
Source20: import-trusted-keys
Source21: import-trusted-keys.service
License: GPG Public Keys

BuildArch: noarch

BuildRequires: systemd
%systemd_requires

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
install -m 0644 %{SOURCE9} %{buildroot}/etc/firstboot.d/data/keys/
install -d %{buildroot}%{_bindir}
install -m 0755 %{SOURCE20} %{buildroot}%{_bindir}/import-trusted-keys
install -d %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE21} %{buildroot}%{_unitdir}/import-trusted-keys.service

%post
%systemd_post import-trusted-keys.service

%preun
%systemd_preun import-trusted-keys.service

%postun
%systemd_postun import-trusted-keys.service

%files
/etc/firstboot.d/data/keys/*
%{_bindir}/import-trusted-keys
%{_unitdir}/import-trusted-keys.service

%changelog
* Wed Jul 15 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.3.7-1.3
- Add import-trusted-keys one-shot service. Replaces old service...
- ... from xenserver-firstboot (60-import-keys)

* Thu Jul 02 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.3.7-1.2
- Rebuild for XCP-ng 8.2
- CH 8.2's proprietary new script and systemd service not imported

* Fri Dec 20 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.3.7-1.1
- Update for XCP-ng 8.1
- Add RPM-GPG-KEY-BRCM-ECD

* Mon Apr 29 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.3.6-1.2
- Rebuild for XCP-ng 8.0

* Thu Jan 24 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.3.6-1.1
- Initial package for XCP-ng.

