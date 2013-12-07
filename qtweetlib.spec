%define	major 1
%define	libqtweetlib %mklibname qtweetlib %{major}
%define develqtweetlib %mklibname -d qtweetlib

Name:		qtweetlib
License:	GPLv2
Version:	0.5.0
Release:	3
Source0:	%{name}-%{version}.tar.gz
Source100:	qtweetlib.rpmlintrc
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
%setup -q -n minimoog-QTweetLib-2af0b78

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


%changelog
* Tue Mar 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.5.0-1
+ Revision: 784598
- version update 0.5.0

* Fri Feb 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.0-1
+ Revision: 780122
- version update 0.4.0

  + Zé <ze@mandriva.org>
    - no need to set requires to release
    - arrange spec

* Fri Nov 25 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.3.0-2
+ Revision: 733370
- release bump
- packages fix in files -n section

* Fri Nov 25 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.3.0-1
+ Revision: 733357
- dependency token fix
- imported package qtweetlib

