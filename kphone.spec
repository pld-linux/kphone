Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Name:		kphone
Version:	4.0.5
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.wirlab.net/kphone/%{name}-%{version}.tar.gz
# Source0-md5:	30939e432fd0039d4dc8228f21e2c54b
Source1:	%{name}.desktop
Patch0:		%{name}-opt.patch
URL:		http://www.wirlab.net/kphone/index.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	libpng-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt-devel >= 3.0
Obsoletes:	kphone-devel
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

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__autoconf}
%configure \
	QTDIR=%{_libdir} \
	--enable-mt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	ICON_DIR=$RPM_BUILD_ROOT%{_datadir}/%{name}/icons

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install -D icons/large-kphone.png $RPM_BUILD_ROOT%{_pixmapsdir}/kphone.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kphone
%{_datadir}/kphone
%{_desktopdir}/kphone.desktop
%{_pixmapsdir}/kphone.png
