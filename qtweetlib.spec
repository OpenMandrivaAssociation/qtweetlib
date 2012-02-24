%define	major 0
%define	libqtweetlib %mklibname qtweetlib %{major}
%define develqtweetlib %mklibname -d qtweetlib

Name:		qtweetlib
License:	GPLv2
Version:	0.4.0
Release:	1
Source0:	%{name}-%{version}.tar.gz
Url:		https://github.com/dschmidt/QTweetLib
Summary:	C++ Qt based Twitter library
Group:		System/Libraries
BuildRequires:	cmake gcc-c++ qt4-devel
BuildRequires:	qjson-devel

%description
C++ Qt based Twitter library.

%package -n %{libqtweetlib}
Group:		System/Libraries
Summary:	C++ Qt based Twitter library

%description -n %{libqtweetlib}
C++ Qt based Twitter library.

%package -n %{develqtweetlib}
Group:		Development/C
Summary:	C++ Qt based Twitter library
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libqtweetlib} = %{version}

%description -n %{develqtweetlib} 
C++ Qt based Twitter library (devel package).

%prep
%setup -q -n minimoog-QTweetLib-aaf2530

%build
%cmake
%make

%install
%makeinstall_std -C build

%files -n %{libqtweetlib}
%{_libdir}/libQTweetLib.so.%{major}*

%files -n %{develqtweetlib}
%{_libdir}/libQTweetLib.so
%{_includedir}/QTweetLib/
