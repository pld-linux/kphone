
Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Name:		kphone
Version:	3.1
Release:	0.9
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.wirlab.net/kphone/%{name}-%{version}.tgz
# Source0-md5:	e2c26a17b5c2514cb5d952699f1c2ec2
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
KPhone jest klientem SIP (Session Initiation Protocol) dla Linuksa,
kt�ry umo�liwia inicjowanie po��cze� VoIP( G�os po IP) poprzez sie�
internet. Od wersji 2.0 dzia�a z Presence i Instant Messaging.

%package devel
Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Group:		Developement

%description devel
Header files for KPhone.

%description -l pl devel
Pliki nag��wkowe dla kphone.

%prep 
%setup -q 

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13 
# crashes build
#	--enable-final \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications

%{__make} DESTDIR=$RPM_BUILD_ROOT install

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
