# TODO:
# - move libs into separate package

Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Name:		kphone
Version:	3.13
Release:	5.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.wirlab.net/kphone/%{name}-%{version}.tgz
# Source0-md5:	42d46da7a2fbce1e9ebf852f543b33ad
URL:		http://www.wirlab.net/kphone/index.html
BuildRequires:	kdelibs-devel >= 3.1.1
BuildRequires:	fam-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPhone is a SIP (Session Initiation Protocol) user agent for Linux,
with which you can initiate VoIP (Voice over IP) connections over the
Internet. The new 2.0 version also supports Presence and Instant
Messaging.

%description -l pl
KPhone jest klientem SIP (Session Initiation Protocol) dla Linuksa,
który umo¿liwia inicjowanie po³±czeñ VoIP( G³os po IP) poprzez sieæ
internet. Od wersji 2.0 dzia³a z Presence i Instant Messaging.

%package devel
Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Group:		Developement

%description devel
Header files for KPhone.

%description devel -l pl
Pliki nag³ówkowe dla kphone.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_icondir="%{_pixmapsdir}"; export kde_icondir


%configure2_13
# crashes build
#	--enable-final \

#%%{__aclocal}
#%%{__autoheader}
#%%{__autoconf}
#%%{__automake}
#%%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/Internet/kphone.desktop $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kphone
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/*.la
%{_applnkdir}/Network/Communications/*.desktop
%{_datadir}/apps/kphone/icons/hicolor/32x32/actions/*.png
%{_pixmapsdir}/*/*/apps/*.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/dissipate2
%{_includedir}/kphonegsm
%{_includedir}/ilbc
