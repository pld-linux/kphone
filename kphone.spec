%bcond_with	jack		# with JACK audio support

Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Name:		kphone
Version:	4.1.1
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.wirlab.net/kphone/%{name}-%{version}.tar.gz
# Source0-md5:	b95252f527e2fbe107f5d3c1159e2e25
Source1:	%{name}.desktop
Patch0:		%{name}-opt.patch
URL:		http://www.wirlab.net/kphone/index.html
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	libpng-devel
BuildRequires:	openssl-devel
BuildRequires:	qt-devel >= 3.0
BuildRequires:	qt-linguist
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
QTDIR="%{_libdir}"; export QTDIR
%configure \
	--enable-jack=%{?with_jack:yes}%{!?with_jack:no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/kphone/{icons,translations}

install kphone/kphone $RPM_BUILD_ROOT%{_bindir}
install icons/*.png $RPM_BUILD_ROOT%{_datadir}/kphone/icons
install po/*.qm $RPM_BUILD_ROOT%{_datadir}/kphone/translations

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install -D icons/large-kphone.png $RPM_BUILD_ROOT%{_pixmapsdir}/kphone.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/kphone
%{_datadir}/kphone/icons
%dir %{_datadir}/kphone/translations
%lang(de) %{_datadir}/kphone/translations/kphone_de.qm
%lang(es) %{_datadir}/kphone/translations/kphone_es_ES.qm
%lang(fi) %{_datadir}/kphone/translations/kphone_fi.qm
%lang(fr) %{_datadir}/kphone/translations/kphone_fr.qm
%lang(hu) %{_datadir}/kphone/translations/kphone_hu.qm
%lang(pt_BR) %{_datadir}/kphone/translations/kphone_pt_BR.qm
%lang(sv) %{_datadir}/kphone/translations/kphone_sv.qm
%{_desktopdir}/kphone.desktop
%{_pixmapsdir}/kphone.png
