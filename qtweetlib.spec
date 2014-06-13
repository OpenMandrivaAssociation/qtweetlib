%define	major 1
%define	libname %mklibname qtweetlib %{major}
%define devname %mklibname -d qtweetlib

Summary:	C++ Qt based Twitter library
Name:		qtweetlib
License:	GPLv2
Version:	0.5.0
Release:	6
Group:		System/Libraries
Url:		https://github.com/dschmidt/QTweetLib
Source0:	%{name}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QJson)

%description
C++ Qt based Twitter library.

%package -n %{libname}
Group:		System/Libraries
Summary:	C++ Qt based Twitter library

%description -n %{libname}
C++ Qt based Twitter library.

%package -n %{devname}
Group:		Development/C
Summary:	C++ Qt based Twitter library
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname} 
C++ Qt based Twitter library (devel package).

%prep
%setup -qn minimoog-QTweetLib-2af0b78

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libQTweetLib.so.%{major}*

%files -n %{devname}
%{_libdir}/libQTweetLib.so
%{_includedir}/QTweetLib/

