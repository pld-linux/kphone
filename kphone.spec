# TODO:
#  - fix ac/am suite
#  - maybe libs should be in separate package?
#  - check if files are layed in system in right way.
#  - make it not segfault on start ;)

Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Name:		kphone
Version:	2.11
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.wirlab.net/kphone/%{name}-%{version}.tgz
URL:		http://www.wirlab.net/kphone/index.html
BuildRequires:	kdelibs-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
KPhone is a SIP (Session Initiation Protocol) user agent for Linux,
with which you can initiate VoIP (Voice over IP) connections over the
Internet. The new 2.0 version also supports Presence and Instant
Messaging.

%description -l pl
KPhone jest klientem SIP (Session Initiation Protocol) dla linuxa,
który umo¿liwia inicjowanie po³±czeñ VoIP( G³os po IP) poprzez sieæ
internet. Od wersji 2.0 dzia³a z Presence i Instant Messaging.

%package devel
Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Group:		Developement

%description devel
Header files for KPhone.

%description -l pl devel
Pliki nag³ówkowe dla kphone.

%prep 
%setup -q -n kphone-2.1

%build
%configure2_13 
# crashes build
#	--enable-final \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} DESTDIR=$RPM_BUILD_ROOT install

mv $RPM_BUILD_ROOT%{_applnkdir}/Internet/kphone.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kphone
%{_libdir}/*.so.*
%{_libdir}/*.la
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/apps/kphone/icons/hicolor/32x32/actions/*.png
%{_datadir}/icons/*/*/apps/*.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/dissipate2/*.h
%{_includedir}/gsm/*.h
%{_includedir}/ilbc/*.h
