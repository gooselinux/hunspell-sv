Name: hunspell-sv
Summary: Swedish hunspell dictionaries
Version: 1.39
Release: 3%{?dist}
Source: http://hem.bredband.net/dsso1/sv-%{version}.zip
Group: Applications/Text
URL: http://dsso.se/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ or GPLv2+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Swedish hunspell dictionaries.

%prep
%setup -q -c -n hunspell-sv

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
sv_SE_aliases="sv_FI"
for lang in $sv_SE_aliases; do
        ln -s sv_SE.aff $lang.aff
        ln -s sv_SE.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_sv_SE.txt

%{_datadir}/myspell/*

%changelog
* Wed Apr 07 2010 Caolan McNamara <caolanm@redhat.com> - 1.30-3
- Resolves: rhbz#580061 clarify licence

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.39-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Caolan McNamara <caolanm@redhat.com> - 1.39-1
- latest version

* Thu Jun 04 2009 Caolan McNamara <caolanm@redhat.com> - 1.38-1
- latest version

* Mon Jun 01 2009 Caolan McNamara <caolanm@redhat.com> - 1.37-1
- latest version

* Tue May 26 2009 Caolan McNamara <caolanm@redhat.com> - 1.35-1
- latest version

* Fri May 22 2009 Caolan McNamara <caolanm@redhat.com> - 1.33-1
- latest version

* Tue May 19 2009 Caolan McNamara <caolanm@redhat.com> - 1.32-1
- latest version

* Mon May 11 2009 Caolan McNamara <caolanm@redhat.com> - 1.31-1
- latest version

* Mon Apr 13 2009 Caolan McNamara <caolanm@redhat.com> - 1.30-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Aug 23 2008 Caolan McNamara <caolanm@redhat.com> - 1.29-1
- latest version
`
* Tue Jun 17 2008 Caolan McNamara <caolanm@redhat.com> - 1.28-1
- latest version

* Wed May 28 2008 Caolan McNamara <caolanm@redhat.com> - 1.27-1
- latest version

* Thu May 13 2008 Caolan McNamara <caolanm@redhat.com> - 1.26-1
- latest version

* Thu Mar 13 2008 Caolan McNamara <caolanm@redhat.com> - 1.25-1
- latest version

* Wed Mar 05 2008 Caolan McNamara <caolanm@redhat.com> - 1.23-1
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 1.22-2
- clarify license version

* Fri Jul 06 2007 Caolan McNamara <caolanm@redhat.com> - 1.22-1
- move to dsso.se dictionaries

* Fri Jul 06 2007 Caolan McNamara <caolanm@redhat.com> - 1.3.8.6b-1
- latest version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 1.3.8.6-1
- initial version
