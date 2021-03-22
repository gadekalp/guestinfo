#
# spec file for package cloud-init-xen-guestinfo
#

#################################################################################
# common
#################################################################################
Name:           cloud-init-xen-guestinfo
Version:        1.3.2
Release:        1.el7
Summary:        A cloud-init datasource that uses Xen GuestInfo
License:        Apache2
Requires:       cloud-init
Group:          Applications/System
BuildArch:      noarch

#################################################################################
# specific
#################################################################################
%description
A cloud-init datasource that uses VMware GuestInfo

%prep

%build

%install
mkdir -p %{buildroot}/
cp -r ./* %buildroot/
exit 0

%clean

%files
%defattr(0644, root,root, 0755)
/etc/cloud/cloud.cfg.d/99-DataSourceXenGuestInfo.cfg
/usr/lib/python2.7/site-packages/cloudinit/sources/DataSourceXenGuestInfo.py
%defattr(0755, root,root)
/usr/bin/dscheck_XenGuestInfo
