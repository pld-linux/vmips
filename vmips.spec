Summary:	Virtual machine simulator based on a MIPS R3000 processor
Summary(pl.UTF-8):	Symulator maszyny wirtualnej opartej na procesorze MIPS R3000
Name:		vmips
Version:	1.5.1
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	https://vmips.sourceforge.net/releases/%{name}-%{version}/vmips-%{version}.tar.gz
# Source0-md5:	6bca35762ff282418e9224ebf7d93583
Patch0:		%{name}-am.patch
Patch1:		%{name}-info.patch
URL:		https://vmips.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vmips is a virtual machine simulator based around a MIPS R3000 RISC
CPU core. It is an open-source project written in GNU C++ and which is
distributed under the GNU General Public License.

%description -l pl.UTF-8
Vmips to symulator maszyny wirtualnej opartej na rdzeniu procesora
RISC MIPS R3000. Jest to projekt z otwartymi źródłami napisany w GNU
C++ i jest rozpowszechniany na licencji GNU GPL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# don't try to rebuild man pages,
# upstream does not provide necessary script
touch doc/*.1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/vmips
%attr(755,root,root) %{_bindir}/vmipstool
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vmipsrc
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/vmips.1*
%{_mandir}/man1/vmipstool.1*
%{_infodir}/vmips.info*
