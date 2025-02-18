#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: e36a856
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kglobalacceld
Version  : 6.3.1
Release  : 22
URL      : https://download.kde.org/stable/plasma/6.3.1/kglobalacceld-6.3.1.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.3.1/kglobalacceld-6.3.1.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.3.1/kglobalacceld-6.3.1.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-3.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kglobalacceld-data = %{version}-%{release}
Requires: kglobalacceld-lib = %{version}-%{release}
Requires: kglobalacceld-license = %{version}-%{release}
Requires: kglobalacceld-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kglobalaccel-dev
BuildRequires : pkgconfig(xcb)
BuildRequires : qt6base-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-image-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the kglobalacceld package.
Group: Data

%description data
data components for the kglobalacceld package.


%package dev
Summary: dev components for the kglobalacceld package.
Group: Development
Requires: kglobalacceld-lib = %{version}-%{release}
Requires: kglobalacceld-data = %{version}-%{release}
Provides: kglobalacceld-devel = %{version}-%{release}
Requires: kglobalacceld = %{version}-%{release}

%description dev
dev components for the kglobalacceld package.


%package lib
Summary: lib components for the kglobalacceld package.
Group: Libraries
Requires: kglobalacceld-data = %{version}-%{release}
Requires: kglobalacceld-license = %{version}-%{release}

%description lib
lib components for the kglobalacceld package.


%package license
Summary: license components for the kglobalacceld package.
Group: Default

%description license
license components for the kglobalacceld package.


%package services
Summary: services components for the kglobalacceld package.
Group: Systemd services
Requires: systemd

%description services
services components for the kglobalacceld package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n kglobalacceld-6.3.1
cd %{_builddir}/kglobalacceld-6.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739916617
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1739916617
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kglobalacceld
cp %{_builddir}/kglobalacceld-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kglobalacceld/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kglobalacceld-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kglobalacceld/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/kglobalacceld-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kglobalacceld/fa05e58320cb7c64786b26396f4b992579a628bc || :
cp %{_builddir}/kglobalacceld-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kglobalacceld/0b71159e19bef95069e18d17296291916e89b5cd || :
cp %{_builddir}/kglobalacceld-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kglobalacceld/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kglobalacceld-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kglobalacceld/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kglobalacceld

%files data
%defattr(-,root,root,-)
/usr/share/xdg/autostart/kglobalacceld.desktop

%files dev
%defattr(-,root,root,-)
/usr/include/KGlobalAccelD/kglobalaccel_interface.h
/usr/include/KGlobalAccelD/kglobalacceld.h
/usr/include/KGlobalAccelD/kglobalacceld_export.h
/usr/lib64/cmake/KGlobalAccelD/KGlobalAccelDConfig.cmake
/usr/lib64/cmake/KGlobalAccelD/KGlobalAccelDConfigVersion.cmake
/usr/lib64/cmake/KGlobalAccelD/KGlobalAccelDTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KGlobalAccelD/KGlobalAccelDTargets.cmake

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKGlobalAccelD.so.0
/usr/lib64/libKGlobalAccelD.so.6.3.1
/usr/lib64/qt6/plugins/org.kde.kglobalacceld.platforms/KGlobalAccelDXcb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kglobalacceld/0b71159e19bef95069e18d17296291916e89b5cd
/usr/share/package-licenses/kglobalacceld/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98
/usr/share/package-licenses/kglobalacceld/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kglobalacceld/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kglobalacceld/fa05e58320cb7c64786b26396f4b992579a628bc

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-kglobalaccel.service
