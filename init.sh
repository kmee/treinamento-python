#!/usr/bin/env bash

virtualenv .

source bin/activate

pip install Sphinx==1.3

pip install hieroglyph sphinx_rtd_theme

sudo apt-get install texlive-lang-portuguese

make dir=docs slides html


