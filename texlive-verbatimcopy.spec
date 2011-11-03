# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/verbatimcopy
# catalog-date 2009-06-02 14:54:30 +0200
# catalog-license lppl
# catalog-version 0.06
Name:		texlive-verbatimcopy
Version:	0.06
Release:	1
Summary:	Make copies of text documents from within LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbatimcopy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimcopy.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimcopy.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides \VerbatimCopy{in}{out} that will enable
LaTeX to take a verbatim copy of one text file, and save it
under another name. The package provides a means to specify the
output directory to be used, but does no checking and may
therefore overwrite an important file if used injudiciously.

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
%{_texmfdistdir}/tex/latex/verbatimcopy/verbatimcopy.sty
%doc %{_texmfdistdir}/doc/latex/verbatimcopy/README
%doc %{_texmfdistdir}/doc/latex/verbatimcopy/verbatimcopy.pdf
%doc %{_texmfdistdir}/doc/latex/verbatimcopy/verbatimcopy.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
