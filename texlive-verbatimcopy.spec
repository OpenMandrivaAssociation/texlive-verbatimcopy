Name:		texlive-verbatimcopy
Version:	15878
Release:	2
Summary:	Make copies of text documents from within LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/verbatimcopy
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimcopy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbatimcopy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides \VerbatimCopy{in}{out} that will enable
LaTeX to take a verbatim copy of one text file, and save it
under another name. The package provides a means to specify the
output directory to be used, but does no checking and may
therefore overwrite an important file if used injudiciously.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verbatimcopy/verbatimcopy.sty
%doc %{_texmfdistdir}/doc/latex/verbatimcopy/README
%doc %{_texmfdistdir}/doc/latex/verbatimcopy/verbatimcopy.pdf
%doc %{_texmfdistdir}/doc/latex/verbatimcopy/verbatimcopy.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
