# revision 23444
# category Package
# catalog-ctan /macros/latex/contrib/tocvsec2
# catalog-date 2010-02-28 10:58:14 +0100
# catalog-license lppl1.3
# catalog-version 1.2b
Name:		texlive-tocvsec2
Version:	1.2b
Release:	2
Summary:	Section numbering and table of contents control
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tocvsec2
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides control over section numbering (without recourse to
starred sectional commands) and/or the entries in the Table of
Contents on a section by section basis.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tocvsec2/tocvsec2.sty
%doc %{_texmfdistdir}/doc/latex/tocvsec2/README
%doc %{_texmfdistdir}/doc/latex/tocvsec2/tocvsec2-example.tex
%doc %{_texmfdistdir}/doc/latex/tocvsec2/tocvsec2.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tocvsec2/tocvsec2.dtx
%doc %{_texmfdistdir}/source/latex/tocvsec2/tocvsec2.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2b-2
+ Revision: 757002
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2b-1
+ Revision: 719773
- texlive-tocvsec2
- texlive-tocvsec2
- texlive-tocvsec2

