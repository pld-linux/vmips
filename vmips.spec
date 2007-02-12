Summary:	Virtual machine simulator based on a MIPS R3000 processor
Summary(pl.UTF-8):   Symulator maszyny wirtualnej opartej na procesorze MIPS R3000
Name:		vmips
Version:	1.3.1
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://vmips.sourceforge.net/releases/%{name}-%{version}/vmips-%{version}.tar.gz
# Source0-md5:	882776097824ed5fe9eaf28220daceca
URL:		http://vmips.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
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

%build
#%%{__gettextize}
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

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/vmipsrc
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_mandir}/*/vmips*
%{_infodir}/vmips*
