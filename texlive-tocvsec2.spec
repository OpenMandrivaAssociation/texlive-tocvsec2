# revision 23444
# category Package
# catalog-ctan /macros/latex/contrib/tocvsec2
# catalog-date 2010-02-28 10:58:14 +0100
# catalog-license lppl1.3
# catalog-version 1.2b
Name:		texlive-tocvsec2
Version:	1.2b
Release:	1
Summary:	Section numbering and table of contents control
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tocvsec2
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides control over section numbering (without recourse to
starred sectional commands) and/or the entries in the Table of
Contents on a section by section basis.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}