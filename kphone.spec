# TODO:
# - move libs into separate package

Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Name:		kphone
Version:	4.0
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.wirlab.net/kphone/%{name}-%{version}.tgz
# Source0-md5:	c27393e931702dac6ecad992acbe3df8
URL:		http://www.wirlab.net/kphone/index.html
BuildRequires:	artsc-devel
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPhone is a SIP (Session Initiation Protocol) user agent for Linux,
with which you can initiate VoIP (Voice over IP) connections over the
Internet. The new 2.0 version also supports Presence and Instant
Messaging.

%description -l pl
KPhone jest klientem SIP (Session Initiation Protocol) dla Linuksa,
który umo¿liwia inicjowanie po³±czeñ VoIP (G³os po IP) poprzez sieæ
internet. Od wersji 2.0 dzia³a z Presence i Instant Messaging.

%package devel
Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for KPhone.

%description devel -l pl
Pliki nag³ówkowe dla kphone.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13 \
	--enable-mt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kdelnkdir=%{_applnkdir}/Network/Communications

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kphone
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/apps/kphone
%{_pixmapsdir}/*/*/apps/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/dissipate2
%{_includedir}/kphonegsm
%{_includedir}/ilbc
