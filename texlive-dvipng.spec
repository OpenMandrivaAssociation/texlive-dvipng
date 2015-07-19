# revision 34145
# category TLCore
# catalog-ctan /dviware/dvipng
# catalog-date 2013-12-16 20:22:01 +0100
# catalog-license lgpl
# catalog-version 1.14
Name:		texlive-dvipng
Version:	1.14
Release:	13
Summary:	A fast DVI to PNG/GIF converter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/dviware/dvipng
License:	LGPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipng.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipng.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-dvipng.bin

%description
This program makes PNG and/or GIF graphics from DVI files as
obtained from TeX and its relatives. Its benefits include:
Speed. It offers very fast rendering of DVI as bitmap files,
which makes it suitable for generating large amounts of images
on-the-fly, as needed in preview-latex, WeBWorK and others; It
does not read the postamble, so it can be started before TeX
finishes. There is a --follow switch that makes dvipng wait at
end-of-file for further output, unless it finds the POST marker
that indicates the end of the DVI; Interactive query of
options. dvipng can read options interactively through stdin,
and all options are usable. It is even possible to change the
input file through this interface. Support for PK, VF,
PostScript Type1, and TrueType fonts, colour specials, and
inclusion of PostScript, PNG, JPEG or GIF images.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/dvipng/dvipng.html
%doc %{_texmfdistdir}/doc/dvipng/dvipng.pdf
%doc %{_infodir}/dvipng.info*
%doc %{_mandir}/man1/dvigif.1*
%doc %{_texmfdistdir}/doc/man/man1/dvigif.man1.pdf
%doc %{_mandir}/man1/dvipng.1*
%doc %{_texmfdistdir}/doc/man/man1/dvipng.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_infodir}
mv %{buildroot}%{_texmfdistdir}/doc/info/*.info %{buildroot}%{_infodir}
