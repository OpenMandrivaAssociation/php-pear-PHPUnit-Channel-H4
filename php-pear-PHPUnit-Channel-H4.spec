%define prj     PHPUnit-Channel
%define	name	php-pear-%{prj}-H4
%define version 1.0
%define release %mkrel 20100211.2
%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define pear_xmldir  %{_libdir}/pear

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Adds pear.phpunit.de channel to PEAR
Group:          System/Libraries
License:        BSD
URL:            https://pear.phpunit.de/
Source0:        http://pear.phpunit.de/pear.phpunit.de.xml
BuildArch:      noarch
BuildRequires:  php-pear >= 5.1.1
Requires:	php-pear >= 5.1.1
Provides:	PHPUnit-Channel-H4


%description
This package provides support for working with feed formats such as RSS and Atom.


%prep
%setup -q -c -T


%build
# Empty build section, nothing to build


%install

%{__mkdir_p} %{buildroot}%{pear_xmldir}
%{__install} -pm 644 %{SOURCE0} %{buildroot}%{pear_xmldir}/pear.horde-H4.org.xml


%clean

%{__rm} -rf %{buildroot}


%post

if [ $1 -eq  1 ] ; then
   pear channel-add %{pear_xmldir}/pear.horde-H4.org.xml > /dev/null || :
else
   pear channel-update %{pear_xmldir}/pear.horde-H4.org.xml > /dev/null ||:
fi


%postun

if [ $1 -eq 0 ] ; then
   pear channel-delete pear.horde-H4.org.xml > /dev/null || :
fi


%files
%defattr(-,root,root,-)
%{pear_xmldir}/pear.horde-H4.org.xml


