Summary:	KPhone - SIP user agent
Summary(pl):	KPhone - Klient SIP
Name:		kphone
Version:	4.0.2
Release:	0.2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://www.wirlab.net/kphone/%{name}-%{version}.tar.gz
# Source0-md5:	106819148c275aaa154c6efe4fcb9d23
Patch0:		%{name}-opt.patch
URL:		http://www.wirlab.net/kphone/index.html
BuildRequires:	artsc-devel
BuildRequires:	autoconf
BuildRequires:	kdelibs-devel
BuildRequires:	openssl-devel >= 0.9.7d
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
	DESTDIR=$RPM_BUILD_ROOT \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	ICON_DIR=$RPM_BUILD_ROOT%{_datadir}/%{name}/icons \
	kdelnkdir=%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kphone
%{_datadir}/kphone
