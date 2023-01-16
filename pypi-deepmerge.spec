#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-deepmerge
Version  : 1.1.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/82/d7/75916d41be4c45a8d9b93d1bb089ac46de0212630641972982023d785d1f/deepmerge-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/82/d7/75916d41be4c45a8d9b93d1bb089ac46de0212630641972982023d785d1f/deepmerge-1.1.0.tar.gz
Summary  : a toolset to deeply merge python dictionaries.
Group    : Development/Tools
License  : MIT
Requires: pypi-deepmerge-license = %{version}-%{release}
Requires: pypi-deepmerge-python = %{version}-%{release}
Requires: pypi-deepmerge-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=========
deepmerge
=========
.. image:: https://github.com/toumorokoshi/deepmerge/actions/workflows/python-package.yaml/badge.svg
:target: https://github.com/toumorokoshi/deepmerge/actions/workflows/python-package.yaml

%package license
Summary: license components for the pypi-deepmerge package.
Group: Default

%description license
license components for the pypi-deepmerge package.


%package python
Summary: python components for the pypi-deepmerge package.
Group: Default
Requires: pypi-deepmerge-python3 = %{version}-%{release}

%description python
python components for the pypi-deepmerge package.


%package python3
Summary: python3 components for the pypi-deepmerge package.
Group: Default
Requires: python3-core
Provides: pypi(deepmerge)

%description python3
python3 components for the pypi-deepmerge package.


%prep
%setup -q -n deepmerge-1.1.0
cd %{_builddir}/deepmerge-1.1.0
pushd ..
cp -a deepmerge-1.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673902575
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-deepmerge
cp %{_builddir}/deepmerge-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-deepmerge/32da40ba47a54da001cc08059c75de858149643b || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-deepmerge/32da40ba47a54da001cc08059c75de858149643b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
