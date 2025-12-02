#!/usr/bin/bash

echo "There is $(find ./source.tex)."
lualatex --shell-escape source.tex
biber source
lualatex --shell-escape source.tex
lualatex --shell-escape source.tex
echo "The task is completed."
