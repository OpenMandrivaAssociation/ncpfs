%define	major		2.3
%define	libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Utilities for the ncpfs filesystem, a NetWare client for Linux
Name:		ncpfs
Version:	2.2.6
Release:	%mkrel 4
License:	GPLv2+
Group:		Networking/Other
URL:		ftp://platan.vc.cvut.cz/pub/linux/ncpfs/
Source0:	ftp://platan.vc.cvut.cz/pub/linux/ncpfs/%{name}-%{version}/%{name}-%{version}.tar.bz2
Patch0:		ncpfs-2.2.3-fix.patch
Patch1:		ncpfs-2.2.3-array.patch
Patch3:		ncpfs-2.2.4-pie.patch
Patch5:		ncpfs-2.2.6-getuid.patch
Patch6:		ncpfs-2.2.4-gcc4.patch
Patch7:		ncpfs-2.2.6-ldconfig.patch
Patch8:		ncpfs-2.2.6-align.patch
Patch9:		ncpfs-2.2.6-add-missing-header.patch
# From Fedora: fixes compilation failure (see Debian bug 428937)
# - AdamW 2007/12
Patch10:	ncpfs-2.2.6-offsetof.patch
Requires:	ipxutils
Requires:	%{libname} = %{version}-%{release}
BuildRequires:	pam-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Ncpfs is a filesystem which understands the Novell NetWare(TM)
NCP protocol.  Functionally, NCP is used for NetWare the way NFS
is used in the TCP/IP world.  For a Linux system to mount a NetWare
filesystem, it needs a special mount program.  The ncpfs package
contains such a mount program plus other tools for configuring and
using the ncpfs filesystem.

Install the ncpfs package if you need to use the ncpfs filesystem
to use Novell NetWare files or services.

%package -n	ipxutils
Summary:	Tools for configuring and debugging IPX interfaces and networks
Group:		System/Configuration/Networking

%description -n	ipxutils
The ipxutils package includes utilities (ipx_configure, ipx_internal_net,
ipx_interface, ipx_route) necessary for configuring and debugging IPX
interfaces and networks under Linux. IPX is the low-level protocol used
by Novell's NetWare file server system to transfer data.

Install ipxutils if you need to configure IPX networking on your network.

%package -n	%{libname}
Summary:	Library associated with ncpfs
Group:		System/Libraries

%description -n	%{libname}
This library is mandatory for ncpfs and ipxutils to run.

%package -n	%{develname}
Summary:	Development package with static libs and headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname ncpfs 2.3 -d}

%description -n	%{develname}
Static libraries and header files required for compiling xmms plugins.

%prep
%setup -q
%patch0 -p1 -b .fix
%patch1 -p1 -b .array
%patch3 -p1 -b .pie
%patch5 -p1 -b .getuid
%patch6 -p1 -b .gcc4
%patch7 -p1 -b .ld
%patch8 -p1 -b .align
%patch9 -p1 -b .header
%patch10 -p1 -b .offset

chmod +rw -R .

%build
chmod -R u+w po
CFLAGS="%{optflags} -fPIC" \
%configure	--disable-rpath \
		--enable-pam

%make clean
%make
%make -C ipxdump
mv ipxdump/README ipxdump/README.ipxdump

%install
rm -rf %{buildroot}

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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
/sbin/mount.ncp*
/sbin/nwmsg
%{_bindir}/n*
%{_bindir}/p*
%{_bindir}/slist
%{_sbindir}/nwmsg
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%doc BUGS Changes FAQ README

%files -n ipxutils
%defattr(-,root,root)
%doc ipx-1.0/COPYING ipx-1.0/README
%doc ipxdump/README.ipxdump
/sbin/ipx_*
%{_bindir}/ipx*
%{_mandir}/*/ipx*

%files -n %{libname}
%defattr(-,root,root)
/lib/security/*
%{_libdir}/libncp.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc Changes
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_includedir}/*

