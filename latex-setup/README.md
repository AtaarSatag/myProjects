This directory contains my \(\LaTeX\) setup/template to build PDF files of different articles and office stuff.

The main config file is `[preamble.sty](https://github.com/AtaarSatag/myprojects/blob/main/latex-setup/preamble.sty)`, which consists of necessary settings, templates, packages, etc.

`[source.tex](https://github.com/AtaarSatag/myprojects/blob/main/latex-setup/source.tex)` is just an example.

`[build-pdf.sh](https://github.com/AtaarSatag/myprojects/blob/main/latex-setup/build-pdf.tex)` is a bash script to build PDF from `[source.tex](https://github.com/AtaarSatag/myprojects/blob/main/latex-setup/source.tex)`. If you change a name of the source, you need to make respetcive changes in the script. Also and of cource, you must have all necessary packages in your TeX environment (see the relevant documentation) to run the script.
