Summary:	A simple and private notes app
Name:		standardnotes-desktop-bin
Version:	3.0.25
Release:	1
License:	AGPL v3+
Group:		Applications
Source0:	https://github.com/standardnotes/desktop/releases/download/v%{version}/Standard-Notes-%{version}.AppImage
# Source0-md5:	cb8bfde5d502d0157c709b1e2aa205af
Source1:	https://github.com/standardnotes/desktop/releases/download/v%{version}/Standard-Notes-%{version}-i386.AppImage
# Source1-md5:	9dbd10e4839caae05a19874608a66e98
URL:		https://github.com/standardnotes/desktop
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# breaks resulting binary
%define	no_install_post_strip 1

%define _enable_debug_packages 0

%description
A free, open-source, and completely encrypted notes app. Mac, PC, &
Linux app repository.

%prep
%setup -qcT

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
%ifarch %{x8664}
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
%endif
%ifarch %{ix86}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
%endif
chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
