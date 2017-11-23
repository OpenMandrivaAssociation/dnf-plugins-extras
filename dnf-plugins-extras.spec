%{!?dnf_lowest_compatible: %global dnf_lowest_compatible 1.1.2}
%{!?dnf_not_compatible: %global dnf_not_compatible 2.0}

# There is no Python 3 version of the DNF API
%bcond_with python3

# OpenMandriva has never used Yum, so we don't need the yum migrator plugin
%bcond_with yum_migrate

# OpenMandriva does not have a useful version of pykickstart
%bcond_with pykickstart

# OpenMandriva does not have snapper
%bcond_with snapper

# OpenMandriva does not have tracer
%bcond_with tracer

Name:		dnf-plugins-extras
Version:	0.0.12
Release:	1
Summary:	Extra Plugins for DNF
Group:		System/Configuration/Packaging
License:	GPLv2+
URL:		https://github.com/rpm-software-management/dnf-plugins-extras
Source0:	https://github.com/rpm-software-management/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# From upstream
Patch0001:	0001-tests-support-set-priority-and-cost-in-RepoStub.patch
Patch0002:	0001-leaves-Reuse-query-instead-of-constructing-fresh-one.patch

# OpenMandriva specific patches
Patch1001:	1001-CMake-Fix-detection-of-Python-2.patch

BuildArch:	noarch
BuildRequires:	cmake
BuildRequires:	gettext

BuildRequires:	python2-dnf >= %{dnf_lowest_compatible}
BuildRequires:	python2-dnf < %{dnf_not_compatible}

BuildRequires:	python2-nose
BuildRequires:	python2-devel

BuildRequires:	python-sphinx

%if %{with pykickstart}
BuildRequires:	python2-kickstart
%endif

%if %{with python3}
BuildRequires:	python-devel
BuildRequires:	python-dnf >= %{dnf_lowest_compatible}
BuildRequires:	python-dnf < %{dnf_not_compatible}
BuildRequires:	python-nose

%if %{with pykickstart}
BuildRequires:	python-kickstart
%endif

%endif

%description
Extra Plugins for DNF.

%package	doc
Summary:	Documentation for Extras Plugins for DNF
Group:		System/Configuration/Packaging

%description doc
Documentation for Extras Plugins for DNF.

%package -n python2-dnf-plugins-extras-common
Summary:	Common files for Extras Plugins for DNF
Group:		System/Configuration/Packaging

Requires:	dnf-plugins-extras-doc = %{version}-%{release}
Requires:	python2-dnf >= %{dnf_lowest_compatible}
Requires:	python2-dnf < %{dnf_not_compatible}
%if %{without python3}
Provides:	dnf-plugins-extras-common = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-common
Common files for Extras Plugins, Python 2 version.

%package -n python2-dnf-plugins-extras-debug
Summary:	Debug Plugin for DNF
Group:		System/Configuration/Packaging

Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}
%if %{without python3}
Provides:	dnf-command(debug-dump)
Provides:	dnf-command(debug-restore)
Provides:	dnf-plugins-extras-debug = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-debug
Debug Plugin for DNF, Python 2 version. Writes system RPM configuration to a dump file
and restores it.

%package -n python2-dnf-plugins-extras-leaves
Summary:	Leaves Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

%if %{without python3}
Provides:	dnf-command(leaves)
Provides:	dnf-plugins-extras-leaves = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-leaves
Leaves Plugin for DNF, Python 2 version. List all installed packages
not required by any other installed package.

%package -n python2-dnf-plugins-extras-local
Summary:	Local Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

Requires:	createrepo_c
%if %{without python3}
Provides:	dnf-plugins-extras-local = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-local
Local Plugin for DNF, Python 2 version. Automatically copy all
downloaded packages to a repository on the local filesystem and
generating repo metadata.

%if %{with yum_migrate}
%package -n python2-dnf-plugins-extras-migrate
Summary:	Migrate Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

Requires:	yum
Requires:	python2-dnf >= %{dnf_lowest_compatible}
Provides:	dnf-command(migrate)
Provides:	dnf-plugins-extras-migrate = %{version}-%{release}

%description -n python2-dnf-plugins-extras-migrate
Migrate Plugin for DNF, Python 2 version. Migrates yum's history, group and
yumdb data to dnf.
%endif

%if %{with pykickstart}
%package -n python2-dnf-plugins-extras-kickstart
Summary:	Kickstart Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

Requires:	python2-kickstart
%if %{without python3}
Provides:	dnf-command(kickstart)
Provides:	dnf-plugins-extras-kickstart = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-kickstart
Kickstart Plugin for DNF, Python 2 version. Install packages listed in a
Kickstart file.
%endif

%package -n python2-dnf-plugins-extras-repoclosure
Summary:	RepoClosure Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

%if %{without python3}
Provides:	dnf-command(repoclosure)
Provides:	dnf-plugins-extras-repoclosure = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-repoclosure
RepoClosure Plugin for DNF, Python 2 version. Display a list of unresolved
dependencies for repositories.

%package -n python2-dnf-plugins-extras-repograph
Summary:	RepoGraph Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

%if %{without python3}
Provides:	dnf-command(repograph)
Provides:	dnf-plugins-extras-repograph = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-repograph
RepoGraph Plugin for DNF, Python 2 version. Output a full package dependency
graph in dot format.

%package -n python2-dnf-plugins-extras-repomanage
Summary:	RepoManage Plugin for DNF
Group:		System/Configuration/Packaging

Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}
%if %{without python3}
Provides:	dnf-command(repomanage)
Provides:	dnf-plugins-extras-repomanage = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-repomanage
RepoManage Plugin for DNF, Python 2 version. Manage a directory of
rpm packages.

%package -n python2-dnf-plugins-extras-show-leaves
Summary:	Leaves Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

Requires:	python2-dnf-plugins-extras-leaves = %{version}-%{release}
%if %{without python3}
Provides:	dnf-plugins-extras-show-leaves = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-show-leaves
Show-leaves Plugin for DNF, Python 2 version. List all installed
packages that are no longer required by any other installed package
after a transaction.

%if %{with snapper}
%package -n python2-dnf-plugins-extras-snapper
Summary:	Snapper Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

Requires:	python2-dbus
Requires:	snapper
%if %{without python3}
Provides:	dnf-plugins-extras-snapper = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-snapper
Snapper Plugin for DNF, Python 2 version. Creates snapshot every transaction.
%endif

%if %{with tracer}
%package -n python2-dnf-plugins-extras-tracer
Summary:	Tracer Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

Requires:	tracer
%if %{without python3}
Provides:	dnf-command(tracer)
Provides:	dnf-plugins-extras-tracer = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-tracer
Tracer Plugin for DNF, Python 2 version. Finds outdated running applications
in your system every transaction.
%endif

%package -n python2-dnf-plugins-extras-versionlock
Summary:	Versionlock Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python2-dnf-plugins-extras-common = %{version}-%{release}

%if %{without python3}
Provides:	dnf-command(versionlock)
Provides:	dnf-plugins-extras-versionlock = %{version}-%{release}
%endif

%description -n python2-dnf-plugins-extras-versionlock
Versionlock plugin takes a set of name/versions for packages and
excludes all other versions of those packages. This allows you to
e.g. protect packages from being updated by newer versions.

%if %{with python3}
%package -n python-dnf-plugins-extras-common
Summary:	Common files for Extras Plugins for DNF
Group:		System/Configuration/Packaging
Requires:	dnf-plugins-extras-doc = %{version}-%{release}
Requires:	python-dnf >= %{dnf_lowest_compatible}
Requires:	python-dnf < %{dnf_not_compatible}
Provides:	dnf-plugins-extras-common = %{version}-%{release}

%description -n python-dnf-plugins-extras-common
Common files for Extras Plugins for DNF, Python 3 version.

%package -n python-dnf-plugins-extras-debug
Summary:	Debug Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Provides:	dnf-command(debug-dump)
Provides:	dnf-command(debug-restore)
Provides:	dnf-plugins-extras-debug = %{version}-%{release}


%description -n python-dnf-plugins-extras-debug
Debug Plugin for DNF, Python 3 version. Writes system RPM configuration to
a dump file and restores it.

%package -n python-dnf-plugins-extras-leaves
Summary:	Leaves Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Provides:	dnf-command(leaves)
Provides:	dnf-plugins-extras-leaves = %{version}-%{release}

%description -n python-dnf-plugins-extras-leaves
Leaves Plugin for DNF, Python 3 version. List all installed packages
not required by any other installed package.

%package -n python-dnf-plugins-extras-local
Summary:	Local Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Requires:	createrepo_c
Provides:	dnf-plugins-extras-local = %{version}-%{release}

%description -n python-dnf-plugins-extras-local
Local Plugin for DNF, Python 3 version. Automatically copy all
downloaded packages to a repository on the local filesystem and
generating repo metadata.

%if %{with pykickstart}
%package -n python-dnf-plugins-extras-kickstart
Summary:	Kickstart Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Requires:	python-kickstart
Provides:	dnf-command(kickstart)
Provides:	dnf-plugins-extras-kickstart = %{version}-%{release}

%description -n python-dnf-plugins-extras-kickstart
Kickstart Plugin for DNF, Python 3 version. Install packages listed in a
Kickstart file.
%endif

%package -n python-dnf-plugins-extras-repoclosure
Summary:	RepoClosure Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Provides:	dnf-command(repoclosure)
Provides:	dnf-plugins-extras-repoclosure = %{version}-%{release}

%description -n python-dnf-plugins-extras-repoclosure
RepoClosure Plugin for DNF, Python 3 version. Display a list of unresolved
dependencies for repositories.

%package -n python-dnf-plugins-extras-repograph
Summary:	RepoGraph Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Provides:	dnf-command(repograph)
Provides:	dnf-plugins-extras-repograph = %{version}-%{release}

%description -n python-dnf-plugins-extras-repograph
RepoGraph Plugin for DNF, Python 3 version. Output a full package dependency
graph in dot format.

%package -n python-dnf-plugins-extras-repomanage
Summary:	RepoManage Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Provides:	dnf-command(repomanage)
Provides:	dnf-plugins-extras-repomanage = %{version}-%{release}


%description -n python-dnf-plugins-extras-repomanage
RepoManage Plugin for DNF, Python 3 version. Manage a directory of
rpm packages.

%package -n python-dnf-plugins-extras-rpmconf
Summary:	RpmConf Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Requires:	python-rpmconf
Provides:	dnf-plugins-extras-rpmconf = %{version}-%{release}

%description -n python-dnf-plugins-extras-rpmconf
RpmConf Plugin for DNF, Python 3 version. Handles .rpmnew, .rpmsave every
transaction.

%package -n python-dnf-plugins-extras-show-leaves
Summary:	Show-leaves Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Requires:	python-dnf-plugins-extras-leaves = %{version}-%{release}
Provides:	dnf-plugins-extras-show-leaves = %{version}-%{release}


%description -n python-dnf-plugins-extras-show-leaves
Show-leaves Plugin for DNF, Python 3 version. List all installed
packages that are no longer required by any other installed package
after a transaction.

%if %{with snapper}
%package -n python-dnf-plugins-extras-snapper
Summary:	Snapper Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Requires:	python-dbus
Requires:	snapper
Provides:	dnf-plugins-extras-snapper = %{version}-%{release}

%description -n python-dnf-plugins-extras-snapper
Snapper Plugin for DNF, Python 3 version. Creates snapshot every transaction.
%endif

%if %{with tracer}
%package -n python-dnf-plugins-extras-tracer
Summary:	Tracer Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Requires:	tracer
Provides:	dnf-command(tracer)
Provides:	dnf-plugins-extras-tracer = %{version}-%{release}

%description -n python-dnf-plugins-extras-tracer
Tracer Plugin for DNF, Python 3 version. Finds outdated running applications
in your system every transaction.
%endif

%package -n python-dnf-plugins-extras-versionlock
Summary:	Versionlock Plugin for DNF
Group:		System/Configuration/Packaging
Requires:	python-dnf-plugins-extras-common = %{version}-%{release}
Provides:	dnf-command(versionlock)
Provides:	dnf-plugins-extras-versionlock = %{version}-%{release}

%description -n python-dnf-plugins-extras-versionlock
Versionlock plugin takes a set of name/versions for packages
and excludes all other versions of those packages. This allows
you to e.g. protect packages from being updated by newer versions.
%endif

%prep
%setup -q -n %{name}-%{version}
%apply_patches

%if %{with python3}
rm -rf py3
mkdir py3
%endif

# Drop the changelog section to keep sphinx from choking
sed -e '564,$ d' -i %{name}.spec

%build
%cmake
%make
make doc-man

%if %{with python3}
pushd ../py3
%cmake -DPYTHON_DESIRED:str=3 ../../
%make
make doc-man
popd
%endif

%install
pushd ./build
%make_install
popd
%if %{with python3}
pushd ./py3/build
%make_install
popd
%endif

%find_lang %{name}

%if %{without yum_migrate}
rm -rf %{buildroot}%{python2_sitelib}/dnf-plugins/migrate.*
rm -rf %{buildroot}%{_mandir}/man8/dnf.plugin.migrate.*
%endif

%if %{without pykickstart}
rm -rf %{buildroot}%{python2_sitelib}/dnf-plugins/kickstart.*
%if %{with python3}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/kickstart.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/kickstart.*
%endif
rm -rf %{buildroot}%{_mandir}/man8/dnf.plugin.kickstart.*
%endif

%if %{without snapper}
rm -rf %{buildroot}%{python2_sitelib}/dnf-plugins/snapper.*
%if %{with python3}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/snapper.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/snapper.*
%endif
rm -rf %{buildroot}%{_mandir}/man8/dnf.plugin.snapper.*
%endif

%if %{without tracer}
rm -rf %{buildroot}%{python2_sitelib}/dnf-plugins/tracer.*
%if %{with python3}
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/tracer.*
rm -rf %{buildroot}%{python3_sitelib}/dnf-plugins/__pycache__/tracer.*
%endif
rm -rf %{buildroot}%{_mandir}/man8/dnf.plugin.tracer.*
%endif

%check
%if %{without pykickstart}
rm -rf tests/test_kickstart.*
%endif

PYTHONPATH="%{buildroot}%{python2_sitelib}:%{buildroot}%{python2_sitelib}/dnf-plugins/" /usr/bin/nosetests-2.* -s tests/
%if %{with python3}
PYTHONPATH="%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitelib}/dnf-plugins/" /usr/bin/nosetests-3.* -s tests/
%endif

%files doc
%doc COPYING AUTHORS README.rst
%{_mandir}/man8/dnf.plugin.*

%files -n python2-dnf-plugins-extras-common -f %{name}.lang
%{python2_sitelib}/dnfpluginsextras/

%files -n python2-dnf-plugins-extras-debug
%{python2_sitelib}/dnf-plugins/debug.*

%files -n python2-dnf-plugins-extras-leaves
%{python2_sitelib}/dnf-plugins/leaves.*

%files -n python2-dnf-plugins-extras-local
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{python2_sitelib}/dnf-plugins/local.*

%if %{with yum_migrate}
%files -n python2-dnf-plugins-extras-migrate
%{python2_sitelib}/dnf-plugins/migrate.*
%endif

%if %{with pykickstart}
%files -n python2-dnf-plugins-extras-kickstart
%{python2_sitelib}/dnf-plugins/kickstart.*
%endif

%files -n python2-dnf-plugins-extras-repoclosure
%{python2_sitelib}/dnf-plugins/repoclosure.*

%files -n python2-dnf-plugins-extras-repograph
%{python2_sitelib}/dnf-plugins/repograph.*

%files -n python2-dnf-plugins-extras-repomanage
%{python2_sitelib}/dnf-plugins/repomanage.*

%files -n python2-dnf-plugins-extras-show-leaves
%{python2_sitelib}/dnf-plugins/show_leaves.*

%if %{with snapper}
%files -n python2-dnf-plugins-extras-snapper
%{python2_sitelib}/dnf-plugins/snapper.*
%endif

%if %{with tracer}
%files -n python2-dnf-plugins-extras-tracer
%{python2_sitelib}/dnf-plugins/tracer.*
%endif

%files -n python2-dnf-plugins-extras-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python2_sitelib}/dnf-plugins/versionlock.*

%if %{with python3}
%files -n python-dnf-plugins-extras-common -f %{name}.lang
%doc AUTHORS COPYING README.rst
%{python3_sitelib}/dnfpluginsextras/
%dir %{python3_sitelib}/dnf-plugins/__pycache__/

%files -n python-dnf-plugins-extras-debug
%{python3_sitelib}/dnf-plugins/debug.*
%{python3_sitelib}/dnf-plugins/__pycache__/debug.*

%files -n python-dnf-plugins-extras-leaves
%{python3_sitelib}/dnf-plugins/leaves.*
%{python3_sitelib}/dnf-plugins/__pycache__/leaves.*

%files -n python-dnf-plugins-extras-local
%config(noreplace) %{_sysconfdir}/dnf/plugins/local.conf
%{python3_sitelib}/dnf-plugins/local.*
%{python3_sitelib}/dnf-plugins/__pycache__/local.*

%if %{with pykickstart}
%files -n python-dnf-plugins-extras-kickstart
%{python3_sitelib}/dnf-plugins/kickstart.*
%{python3_sitelib}/dnf-plugins/__pycache__/kickstart.*
%endif

%files -n python-dnf-plugins-extras-repoclosure
%{python3_sitelib}/dnf-plugins/repoclosure.*
%{python3_sitelib}/dnf-plugins/__pycache__/repoclosure.*

%files -n python-dnf-plugins-extras-repograph
%{python3_sitelib}/dnf-plugins/repograph.*
%{python3_sitelib}/dnf-plugins/__pycache__/repograph.*

%files -n python-dnf-plugins-extras-repomanage
%{python3_sitelib}/dnf-plugins/repomanage.*
%{python3_sitelib}/dnf-plugins/__pycache__/repomanage.*

%files -n python-dnf-plugins-extras-rpmconf
%{python3_sitelib}/dnf-plugins/rpm_conf.*
%{python3_sitelib}/dnf-plugins/__pycache__/rpm_conf.*

%files -n python-dnf-plugins-extras-show-leaves
%{python3_sitelib}/dnf-plugins/show_leaves.*
%{python3_sitelib}/dnf-plugins/__pycache__/show_leaves.*

%if %{with snapper}
%files -n python-dnf-plugins-extras-snapper
%{python3_sitelib}/dnf-plugins/snapper.*
%{python3_sitelib}/dnf-plugins/__pycache__/snapper.*
%endif

%if %{with tracer}
%files -n python-dnf-plugins-extras-tracer
%{python3_sitelib}/dnf-plugins/tracer.*
%{python3_sitelib}/dnf-plugins/__pycache__/tracer.*
%endif

%files -n python-dnf-plugins-extras-versionlock
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.conf
%config(noreplace) %{_sysconfdir}/dnf/plugins/versionlock.list
%{python3_sitelib}/dnf-plugins/versionlock.*
%{python3_sitelib}/dnf-plugins/__pycache__/versionlock.*
%endif

