%global tl_name dvipng
%global tl_revision 77830

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.18
Release:	%{tl_revision}.1
Summary:	A fast DVI to PNG/GIF converter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/dviware/dvipng
License:	lgpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipng.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dvipng.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dvipng.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This program makes PNG and/or GIF graphics from DVI files as obtained
from TeX and its relatives. Its benefits include: Speed. It offers very
fast rendering of DVI as bitmap files, which makes it suitable for
generating large amounts of images on-the-fly, as needed in preview-
latex, WeBWorK and others; It does not read the postamble, so it can be
started before TeX finishes. There is a --follow switch that makes
dvipng wait at end-of-file for further output, unless it finds the POST
marker that indicates the end of the DVI; Interactive query of options.
dvipng can read options interactively through stdin, and all options are
usable. It is even possible to change the input file through this
interface. Support for PK, VF, PostScript Type1, and TrueType fonts,
colour specials, and inclusion of PostScript, PNG, JPEG or GIF images.

