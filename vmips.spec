Summary:	Virtual machine simulator based on a MIPS R3000 processor
Summary(pl):	Symulator maszyny wirtualnej opartej na procesorze MIPS R3000
Name:		vmips
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://vmips.sourceforge.net/releases/vmips-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2000798014259002759c19a27f320c9e
# Source0-size:	1086275
URL:		http://vmips.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vmips is a virtual machine simulator based around a MIPS R3000 RISC
CPU core. It is an open-source project written in GNU C++ and which is
distributed under the GNU General Public License.

%description -l pl
Vmips to symulator maszyny wirtualnej opartej na rdzeniu procesora
RISC MIPS R3000. Jest to projekt z otwartymi ¼ród³ami napisany w GNU
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
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/vmipsrc
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_mandir}/*/vmips* 
%{_infodir}/vmips*
