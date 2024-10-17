Name:		texlive-tocvsec2
Version:	33146
Release:	2
Summary:	Section numbering and table of contents control
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tocvsec2
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocvsec2.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
