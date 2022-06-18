Name:           scan
Version:        1.0
Release:        1.0
Summary:        port scan
BuildArch:      noarch

License:        GPL
Source:        %{name}-%{version}.tar.gz

%description
A port scan RPM %{_bindir}

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/%{name}
cp index.html $RPM_BUILD_ROOT/%{_bindir}/%{name}
cp __init__.py $RPM_BUILD_ROOT/%{_bindir}/%{name}
cp main.py $RPM_BUILD_ROOT/%{_bindir}/%{name}
cp requirements.txt $RPM_BUILD_ROOT/%{_bindir}/%{name}
cp test.py $RPM_BUILD_ROOT/%{_bindir}/%{name}
cp urls.py $RPM_BUILD_ROOT/%{_bindir}/%{name}
cp views.py $RPM_BUILD_ROOT/%{_bindir}/%{name}


%files
%{_bindir}/%{name}/index.html
%{_bindir}/%{name}/__init__.py
%{_bindir}/%{name}/main.py
%{_bindir}/%{name}/requirements.txt
%{_bindir}/%{name}/test.py
%{_bindir}/%{name}/urls.py
%{_bindir}/%{name}/views.py

%changelog
* Sat Jun  18 2022 Nikolai Vetoshkin <nikolai.vetoshkin6@gmail.com> - 1.0.0
- First version being packaged
