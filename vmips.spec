Summary:	Virtual machine simulator based on a MIPS R3000 processor.
Name:		vmips
Version:	1.2.1
Release:	0.1
License:	GPL
Group:		Applications/Emulators
Source0:	http://vmips.sourceforge.net/releases/vmips-%{version}/%{name}-%{version}.tar.gz
#Source0-MD5:	d1f18690c3017536436e72a7e94e3421
URL:		http://vmips.sourceforge.net
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vmips is a virtual machine simulator based around a MIPS R3000 RISC CPU
core. It is an open-source project written in GNU C++ and which is
distributed under the GNU General Public License.

%prep
%setup -q 

%build
rm -f missing
#%%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%files
%defattr(644,root,root,755)
%doc ChangeLog README 
%{_mandir}/*/vmips* 
%{_infodir}/vmips*
/etc/vmipsrc
%attr(755,root,root) %{_bindir}/*
