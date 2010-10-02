name: unldif
summary: Unfold LDIF (LDAP Data Interchange Format) lines
group: Applications/Internet

version: 1.0
release: 0

url: http://vgoenka.tripod.com/unixscripts/unldif.sed.txt
license: Attribution (see COPYING)
source: %{name}-%{version}.tar.gz
buildarch: noarch
buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

buildrequires: asciidoc

requires: sed

%description
Most LDIF generators will fold a long field on multiple lines by
inserting a line separator (either a linefeed or carriage
return/linefeed pair) followed by a space. Processing such ldif
files through another script becomes much easier if such lines were
unfolded. That is exactly what this script does. It unfolds ldif
entries that are folded (broken) across lines and writes them on a
single line.


%prep
%setup -q


%clean
%{__rm} -fr %{buildroot}


%build
# convert manpage
/usr/bin/a2x -d manpage -f manpage doc/unldif.1.asciidoc


%install
%{__rm} -fr %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m755 src/unldif.sed %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__gzip} -c doc/unldif.1 > %{buildroot}/%{_mandir}/man1/unldif.1.gz


%files
%defattr(-,root,root,-)
%{_bindir}/unldif.sed
%doc doc/COPYING
%doc %{_mandir}/man1/unldif.1.gz


%changelog