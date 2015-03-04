Name:           ros-hydro-rtsprofile
Version:        3.0.3
Release:        2%{?dist}
Summary:        ROS rtsprofile package

Group:          Development/Libraries
License:        EPL
URL:            http://ros.org/wiki/openrtm_tools
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  omniORB-devel
BuildRequires:  python-omniORB
BuildRequires:  python-setuptools
BuildRequires:  ros-hydro-catkin

%description
Library to read, manipulate and write RT system profiles using the RTSProfile
XML schema.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Mar 04 2015 Kei OKada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.0.3-2
- Autogenerated by Bloom

* Tue Feb 10 2015 Kei OKada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-1
- Autogenerated by Bloom

* Tue Feb 10 2015 Kei OKada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom
