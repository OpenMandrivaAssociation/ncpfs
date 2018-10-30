%define	major	2.3
%define	libname	%mklibname ncp %{major}
%define	devname	%mklibname ncp -d

%define _disable_lto 1

Summary:	Utilities for the ncpfs filesystem, a NetWare client for Linux
Name:		ncpfs
Version:	2.2.6
Release:	25
License:	GPLv2+
Group:		Networking/Other
Url:		ftp://platan.vc.cvut.cz/pub/linux/ncpfs/
Source0:	ftp://platan.vc.cvut.cz/pub/linux/ncpfs/%{name}-%{version}/%{name}-%{version}.tar.bz2
Patch403:       ncpfs-hg-commit-403.patch
Patch404:       ncpfs-hg-commit-404.patch
Patch405:       ncpfs-hg-commit-405.patch
Patch406:       ncpfs-hg-commit-406.patch
Patch407:       ncpfs-hg-commit-407.patch
Patch408:       ncpfs-hg-commit-408.patch
Patch409:       ncpfs-hg-commit-409.patch
Patch410:       ncpfs-hg-commit-410.patch
Patch411:       ncpfs-hg-commit-411.patch
Patch412:       ncpfs-hg-commit-412.patch
Patch413:       ncpfs-hg-commit-413.patch
Patch414:       ncpfs-hg-commit-414.patch
Patch415:       ncpfs-hg-commit-415.patch
Patch416:       ncpfs-hg-commit-416.patch
Patch417:       ncpfs-hg-commit-417.patch
Patch419:       ncpfs-hg-commit-419.patch
Patch420:       ncpfs-hg-commit-420.patch
Patch421:       ncpfs-hg-commit-421.patch
Patch422:       ncpfs-hg-commit-422.patch
Patch423:       ncpfs-hg-commit-423.patch
Patch424:       ncpfs-hg-commit-424.patch
Patch425:       ncpfs-hg-commit-425.patch
Patch426:       ncpfs-hg-commit-426.patch
Patch427:       ncpfs-hg-commit-427.patch
Patch428:       ncpfs-hg-commit-428.patch
Patch429:       ncpfs-hg-commit-429.patch
Patch430:       ncpfs-hg-commit-430.patch
Patch431:       ncpfs-hg-commit-431.patch
Patch432:       ncpfs-hg-commit-432.patch
Patch433:       ncpfs-hg-commit-433.patch
Patch434:       ncpfs-hg-commit-434.patch
Patch435:       ncpfs-hg-commit-435.patch
Patch436:       ncpfs-hg-commit-436.patch
Patch437:       ncpfs-hg-commit-437.patch
Patch438:       ncpfs-hg-commit-438.patch
Patch439:       ncpfs-hg-commit-439.patch
Patch440:       ncpfs-hg-commit-440.patch
Patch441:       ncpfs-hg-commit-441.patch
Patch442:       ncpfs-hg-commit-442.patch
Patch443:       ncpfs-hg-commit-443.patch
Patch444:       ncpfs-hg-commit-444.patch
Patch445:       ncpfs-hg-commit-445.patch
Patch446:       ncpfs-hg-commit-446.patch
Patch447:       ncpfs-hg-commit-447.patch
Patch448:       ncpfs-hg-commit-448.patch
Patch449:       ncpfs-hg-commit-449.patch
Patch450:       ncpfs-hg-commit-450.patch
Patch451:       ncpfs-hg-commit-451.patch
Patch452:       ncpfs-hg-commit-452.patch
Patch453:       ncpfs-hg-commit-453.patch
Patch454:       ncpfs-hg-commit-454.patch
Patch455:       ncpfs-hg-commit-455.patch
Patch456:       ncpfs-hg-commit-456.patch
Patch457:       ncpfs-hg-commit-457.patch
Patch458:       ncpfs-hg-commit-458.patch
Patch1002:      ncpfs.LDFLAGS.patch
Patch1003:      ncpfs.pam_ncp_auth.syslog.patch
Patch1005:      ncpfs.offsetof.patch
Patch1006:      ncpfs.mount_hang.patch
Patch1007:      ncpfs-2.2.6-mount-issue-ver2.patch
Patch1008:      ncpfs-2_2_6_partial.patch
Patch1009:      ncpfs-2.2.6-CVE-2011-1679,1680.diff
Requires:	ipxutils
BuildRequires:	pam-devel

%description
Ncpfs is a filesystem which understands the Novell NetWare(TM) NCP protocol.
Functionally, NCP is used for NetWare the way NFS is used in the TCP/IP world.
For a Linux system to mount a NetWare filesystem, it needs a special mount
program. The ncpfs package contains such a mount program plus other tools for
configuring and using the ncpfs filesystem.

Install the ncpfs package if you need to use the ncpfs filesystem to use Novell
NetWare files or services.

%package -n	ipxutils
Summary:	Tools for configuring and debugging IPX interfaces and networks
Group:		System/Configuration/Networking

%description -n	ipxutils
The ipxutils package includes utilities (ipx_configure, ipx_internal_net,
ipx_interface, ipx_route) necessary for configuring and debugging IPX
interfaces and networks under Linux. IPX is the low-level protocol used by
Novell's NetWare file server system to transfer data.

Install ipxutils if you need to configure IPX networking on your network.

%package -n	%{libname}
Summary:	Library associated with ncpfs
Group:		System/Libraries
Obsoletes:	%{_lib}ncpfs2.3 < 2.2.6-14

%description -n	%{libname}
This library is mandatory for ncpfs and ipxutils to run.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}ncpfs-devel < 2.2.6-14

%description -n	%{devname}
Development files for %{name}

%prep
%setup -q
%patch403 -p1
%patch404 -p1
%patch405 -p1
%patch406 -p1
%patch407 -p1
%patch408 -p1
%patch409 -p1
%patch410 -p1
%patch411 -p1
%patch412 -p1
%patch413 -p1
%patch414 -p1
%patch415 -p1
%patch416 -p1
%patch417 -p1
%patch419 -p1
%patch420 -p1
%patch421 -p1
%patch422 -p1
%patch423 -p1
%patch424 -p1
%patch425 -p1
%patch426 -p1
%patch427 -p1
%patch428 -p1
%patch429 -p1
%patch430 -p1
%patch431 -p1
%patch432 -p1
%patch433 -p1
%patch434 -p1
%patch435 -p1
%patch436 -p1
%patch437 -p1
%patch438 -p1
%patch439 -p1
%patch440 -p1
%patch441 -p1
%patch442 -p1
%patch443 -p1
%patch444 -p1
%patch445 -p1
%patch446 -p1
%patch447 -p1
%patch448 -p1
%patch449 -p1
%patch450 -p1
%patch451 -p1
%patch452 -p1
%patch453 -p1
%patch454 -p1
%patch455 -p1
%patch456 -p1
%patch457 -p1
%patch458 -p1
#
%patch1002 -p1
%patch1003 -p1
%patch1005 -p1
%patch1006 -p1
%patch1007 -p1
%patch1008 -p1
%patch1009 -p1

chmod +rw -R .

# lib64 fix
perl -pi -e "s|/lib/security\b|/%{_lib}/security|g" configure*

%build
chmod -R u+w po

CFLAGS="%{optflags} -fPIC" \
LDFLAGS="%{ldflags}" \
%configure2_5x \
	--disable-rpath \
	--enable-pam

%make clean
%make

%make -C ipxdump
mv ipxdump/README ipxdump/README.ipxdump

%install
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_libdir}

%makeinstall_std install-dev

# Move ipx_configure/ipx_internal_net to permit /usr from NFS
for i in ipx_configure ipx_internal_net ipx_interface ; do
    mv %{buildroot}%{_bindir}/$i %{buildroot}/sbin/$i
done

install -m755 ipxdump/ipxdump ipxdump/ipxparse %{buildroot}%{_bindir}/

ln -sf ncpmount.8 %{buildroot}%{_mandir}/man8/mount.ncp.8

%find_lang %{name}

#rm -f %{buildroot}/usr/share/locale/locale.alias

rm -f %{buildroot}%{_libdir}/*.*a

%post -n ipxutils
if [ -f %{_sysconfdir}/modules.conf ];then
    if ! grep -q -E "^alias.*net-pf-4.*ipx" %{_sysconfdir}/modules.conf;then
	echo "alias net-pf-4 ipx" >> %{_sysconfdir}/modules.conf
    fi
else
    echo "alias net-pf-4 ipx" >> %{_sysconfdir}/modules.conf
fi

%postun  -n ipxutils
if [ "$1" = "0" ];then
    if [ -f %{_sysconfdir}/modules.conf ];then
	if grep -q -E "^alias.*net-pf-4.*ipx" %{_sysconfdir}/modules.conf;then
	    sed 's/^alias net-pf-4 ipx//' %{_sysconfdir}/modules.conf > /tmp/.modules.conf \
	    && mv -f /tmp/.modules.conf %{_sysconfdir}/modules.conf
	fi
    fi
fi


%files -f %{name}.lang
%doc BUGS Changes FAQ README
/sbin/mount.ncp*
/sbin/nwmsg
%{_bindir}/n*
%{_bindir}/p*
%{_bindir}/slist
%{_sbindir}/nwmsg
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/mount.ncp.8*
%{_mandir}/man8/ncplogin.8*
%{_mandir}/man8/ncpmap.8*
%{_mandir}/man8/ncpmount.8*
%{_mandir}/man8/ncpumount.8*
%{_mandir}/man8/nwbocreate.8*
%{_mandir}/man8/nwborm.8*
%{_mandir}/man8/nwbpadd.8*
%{_mandir}/man8/nwbpcreate.8*
%{_mandir}/man8/nwbprm.8*
%{_mandir}/man8/nwfsctrl.8*
%{_mandir}/man8/nwgrant.8*
%{_mandir}/man8/nwmsg.8*
%{_mandir}/man8/nwrevoke.8*

%files -n ipxutils
%doc ipx-1.0/COPYING ipx-1.0/README
%doc ipxdump/README.ipxdump
/sbin/ipx_configure
/sbin/ipx_interface
/sbin/ipx_internal_net
%{_bindir}/ipx_cmd
%{_bindir}/ipx_route
%{_bindir}/ipxdump
%{_bindir}/ipxparse
%{_mandir}/man8/ipx_cmd.8*
%{_mandir}/man8/ipx_configure.8*
%{_mandir}/man8/ipx_interface.8*
%{_mandir}/man8/ipx_internal_net.8*
%{_mandir}/man8/ipx_route.8*

%files -n %{libname}
/%{_lib}/security/*
%{_libdir}/libncp.so.%{major}*

%files -n %{devname}
%doc Changes
%{_libdir}/lib*.so
%{_includedir}/*

