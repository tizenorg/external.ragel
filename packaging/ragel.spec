Name:       ragel
Summary:    Ragel
Version:    6.6
Release:    1
Group:      TO_BE/FILLED_IN
License:    TO BE FILLED IN
Source0:    %{name}-%{version}.tar.gz
Patch0:  no-doc.patch


%description


%prep
%setup -q 
%patch0 -p1


%build
./autogen.sh
./configure --prefix=%{_prefix}


make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install



%files
/usr/bin/ragel
/usr/share/doc/ragel/CREDITS
/usr/share/doc/ragel/ChangeLog

