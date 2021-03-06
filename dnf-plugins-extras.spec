%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 4.4.3}
%global dnf_plugins_extra_obsolete 2.0.0

# OpenMandriva does not have a useful version of pykickstart
%bcond_with pykickstart

# OpenMandriva does not have rpmconf
%bcond_without rpmconf

# OpenMandriva does not have snapper
%bcond_with snapper

# OpenMandriva does not have tracer
%bcond_with tracer

Name:		dnf-plugins-extras
Version:	4.0.15
Release:	1
Summary:	Extras Plugins for DNF
Group:		System/Configuration/Packaging
License:	GPLv2+
URL:		https://github.com/rpm-software-management/%{name}
Source0:	https://github.com/rpm-software-management/dnf-plugins-extras/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		dnf-plugins-core-4.0.4-sphinx-build.patch

BuildArch:	noarch
BuildRequires:	cmake
BuildRequires:	gettext
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python-dnf >= %{dnf_lowest_compatible}
BuildRequires:	python-nose
BuildRequires:	python-sphinx

%description
Extras Plugins for DNF.

%package -n python-%{name}-common
Summary:	Common files for Extras Plugins for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf >= %{dnf_lowest_compatible}
Provides:	%{name}-common = %{version}-%{release}
Obsoletes:	%{name}-common < %{version}-%{release}
Obsoletes:	python-%{name}-common < %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}
Obsoletes:	%{name}-common-data < %{version}-%{release}
Conflicts:	python2-%{name}-common < %{version}-%{release}

%description -n python-%{name}-common
Common files for Extras Plugins for DNF, Python 3 version.

%if %{with pykickstart}
%package -n python-dnf-plugin-kickstart
Summary:	Kickstart Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name}-common = %{version}-%{release}
BuildRequires:	python-kickstart
Requires:	python-kickstart
Provides:	dnf-command(kickstart)
Provides:	%{name}-kickstart = %{version}-%{release}
Provides:	dnf-plugin-kickstart = %{version}-%{release}
Provides:	python-%{name}-kickstart = %{version}-%{release}
Conflicts:	python2-dnf-plugin-kickstart < %{version}-%{release}
Obsoletes:	python-%{name}-kickstart < %{dnf_plugins_extra_obsolete}

%description -n python-dnf-plugin-kickstart
Kickstart Plugin for DNF, Python 3 version. Install packages listed in a
Kickstart file.
%endif

%if %{with rpmconf}
%package -n python-dnf-plugin-rpmconf
Summary:	RpmConf Plugin for DNF
Group:		System/Configuration/Packaging
BuildRequires:	python-rpmconf
Requires:	python-%{name}-common = %{version}-%{release}
Requires:	python-rpmconf
Provides:	%{name}-rpmconf = %{version}-%{release}
Provides:	dnf-plugin-rpmconf = %{version}-%{release}
Provides:	python-%{name}-rpmconf = %{version}-%{release}
Obsoletes:	python-%{name}-rpmconf < %{dnf_plugins_extra_obsolete}

%description -n python-dnf-plugin-rpmconf
RpmConf Plugin for DNF, Python 3 version. Handles .rpmnew, .rpmsave every
transaction.
%endif

%if %{with snapper}
%package -n python-dnf-plugin-snapper
Summary:	Snapper Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name}-common = %{version}-%{release}
Requires:	python-dbus
Requires:	snapper
Provides:	%{name}-snapper = %{version}-%{release}
Provides:	dnf-plugin-snapper = %{version}-%{release}
Provides:	python-%{name}-snapper = %{version}-%{release}
Conflicts:	python2-dnf-plugin-snapper < %{version}-%{release}
Obsoletes:	python-%{name}-snapper < %{dnf_plugins_extra_obsolete}

%description -n python-dnf-plugin-snapper
Snapper Plugin for DNF, Python 3 version. Creates snapshot every transaction.
%endif

%package -n python-dnf-plugin-system-upgrade
Summary:	System Upgrade Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name}-common = %{version}-%{release}
Requires:	python-systemd
Provides:	dnf-command(system-upgrade)
Provides:	dnf-command(offline-upgrade)
Provides:	dnf-command(offline-distrosync)
Provides:	%{name}-system-upgrade = %{version}-%{release}
Provides:	system-upgrade = %{version}-%{release}
Provides:	dnf-plugin-system-upgrade = %{version}-%{release}
Provides:	python-%{name}-system-upgrade = %{version}-%{release}
Obsoletes:	python-%{name}-system-upgrade < %{dnf_plugins_extra_obsolete}
Obsoletes:	fedup < 0.9.4
Obsoletes:	dnf-plugin-system-upgrade < 0.10
Conflicts:	python2-dnf-plugin-system-upgrade < %{version}-%{release}
BuildRequires:	systemd-macros
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	python-systemd
BuildRequires:	python3dist(systemd-python)
%{?systemd_requires}

%description -n python-dnf-plugin-system-upgrade
System Upgrade Plugin for DNF, Python 3 version. Enables offline system upgrades and distrosync
using three commands: ``system-upgrade``, ``offline-upgrade``, and ``offline-distrosync``.

%if %{with tracer}
%package -n python-dnf-plugin-tracer
Summary:	Tracer Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name}-common = %{version}-%{release}
Requires:	python-tracer >= 0.6.12
Provides:	dnf-plugin-tracer = %{version}-%{release}
Provides:	%{name}-tracer = %{version}-%{release}
Provides:	python-%{name}-tracer = %{version}-%{release}
Conflicts:	python2-dnf-plugin-tracer < %{version}-%{release}
Obsoletes:	python-%{name}-tracer < %{dnf_plugins_extra_obsolete}

%description -n python-dnf-plugin-tracer
Tracer Plugin for DNF, Python 3 version. Finds outdated running applications in
your system every transaction.
%endif

%package -n python-dnf-plugin-torproxy
Summary:	Tor Proxy Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name}-common = %{version}-%{release}
Requires:	python-pycurl
Provides:	dnf-plugin-torproxy = %{version}-%{release}
Provides:	%{name}-torproxy = %{version}-%{release}
Provides:	python-%{name}-torproxy = %{version}-%{release}
Obsoletes:	python-%{name}-torproxy < %{dnf_plugins_extra_obsolete}

%description -n python-dnf-plugin-torproxy
Tor proxy plugin forces DNF to use Tor to download packages. It makes sure that
Tor is working and avoids leaking the hostname by using the proper SOCKS5 interface.

%package -n python-dnf-plugin-showvars
Summary:	Showvars Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-%{name}-common = %{version}-%{release}
Provides:	dnf-plugin-showvars = %{version}-%{release}
Provides:	%{name}-showvars = %{version}-%{release}
Provides:	python-%{name}-showvars = %{version}-%{release}

%description -n python-dnf-plugin-showvars
This plugin dumps the current value of any defined DNF variables.  For example
$releasever and $basearch.

%prep
%autosetup -n %{name}-%{version}%{?prerel:-%{prerel}} -p1

%build
%cmake -DPYTHON_DESIRED:str=3
%make_build
make doc-man

%install
%make_install -C build

mkdir -p %{buildroot}%{_unitdir}/system-update.target.wants/
cd %{buildroot}%{_unitdir}/system-update.target.wants/
  ln -sr ../dnf-system-upgrade.service
cd -

%find_lang %{name}

%if ! %{with pykickstart}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/kickstart.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/kickstart.*
rm -rf %{buildroot}%{_mandir}/man8/dnf-kickstart.*
%endif

%if ! %{with rpmconf}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/rpmconf.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/rpm_conf.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/rpmconf.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/rpm_conf.*
rm -rf %{buildroot}%{_sysconfdir}/dnf/plugins/rpmconf.conf
rm -rf %{buildroot}%{_mandir}/man8/dnf-rpmconf.*
%endif

%if ! %{with snapper}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/snapper.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/snapper.*
rm -rf %{buildroot}%{_mandir}/man8/dnf-snapper.*
%endif

%if ! %{with tracer}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/tracer.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/tracer.*
rm -rf %{buildroot}%{_mandir}/man8/dnf-tracer.*
%endif

%check
%if ! %{with pykickstart}
rm -rf tests/test_kickstart.*
%endif

%if ! %{with rpmconf}
rm -rf tests/test_rpmconf.*
%endif

PYTHONPATH="%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitelib}/dnf-plugins/" nosetests-%{python3_version} -s tests/

%files -n python-%{name}-common -f %{name}.lang
%{python3_sitelib}/dnfpluginsextras/
%license COPYING
%doc AUTHORS README.rst

%if %{with pykickstart}
%files -n python-dnf-plugin-kickstart
%{python3_sitelib}/dnf-plugins/kickstart.*
%{python3_sitelib}/dnf-plugins/__pycache__/kickstart.*
%{_mandir}/man8/dnf-kickstart.*
%endif

%if %{with rpmconf}
%files -n python-dnf-plugin-rpmconf
%config(noreplace) %{_sysconfdir}/dnf/plugins/rpmconf.conf
%{python3_sitelib}/dnf-plugins/rpm_conf.*
%{python3_sitelib}/dnf-plugins/__pycache__/rpm_conf.*
%{_mandir}/man8/dnf-rpmconf.*
%endif

%if %{with snapper}
%files -n python-dnf-plugin-snapper
%{python3_sitelib}/dnf-plugins/snapper.*
%{python3_sitelib}/dnf-plugins/__pycache__/snapper.*
%{_mandir}/man8/dnf-snapper.*
%endif

%files -n python-dnf-plugin-system-upgrade
%{_unitdir}/dnf-system-upgrade.service
%{_unitdir}/system-update.target.wants/dnf-system-upgrade.service
%{_unitdir}/dnf-system-upgrade-cleanup.service
%{python3_sitelib}/dnf-plugins/system_upgrade.py
%{python3_sitelib}/dnf-plugins/__pycache__/system_upgrade*.pyc
%{_mandir}/man8/dnf-system-upgrade.*

%if %{with tracer}
%files -n python-dnf-plugin-tracer
%{python3_sitelib}/dnf-plugins/tracer.*
%{python3_sitelib}/dnf-plugins/__pycache__/tracer.*
%{_mandir}/man8/dnf-tracer.*
%endif

%files -n python-dnf-plugin-torproxy
%config(noreplace) %{_sysconfdir}/dnf/plugins/torproxy.conf
%{python3_sitelib}/dnf-plugins/torproxy.*
%{python3_sitelib}/dnf-plugins/__pycache__/torproxy*.pyc
%{_mandir}/man8/dnf-torproxy.*

%files -n python-dnf-plugin-showvars
%{python3_sitelib}/dnf-plugins/showvars.*
%{python3_sitelib}/dnf-plugins/__pycache__/showvars.*
%{_mandir}/man8/dnf-showvars.*
