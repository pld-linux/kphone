
# TODO:
#  - consider using configure macros.
#  - check if files are layed in system in right way.
#  - make it not segfault on start ;)

Summary:	KPhone - SIP user agent.
Summary(pl):	KPhone - Klient SIP.
Name:		kphone
Version:	2.1
Release:	0.1
License:	Uknown
Group:		Applications/Communications
Source0:	http://www.wirlab.net/kphone/%{name}-%{version}.tgz
URL:		http://www.wirlab.net/kphone/index.html

BuildRequires:	kdelibs-devel
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

%prep
%setup -q

%build
#%%{__autoconf}
#%%configure
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/share
mv $RPM_BUILD_ROOT%{_datadir}/* $RPM_BUILD_ROOT%{_prefix}/X11R6/share

install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/share/applnk/Network/Communications
mv $RPM_BUILD_ROOT%{_prefix}/X11R6/share/applnk/Internet/kphone.desktop $RPM_BUILD_ROOT%{_prefix}/X11R6/share/applnk/Network/Communications/

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kphone
%{_libdir}/*.so.*
%{_prefix}/X11R6/share/*
