#!/bin/bash

if [ "$#" -eq 0 ]
then
  echo "usage: $0 <PDFnames>"
  echo ""
  exit 1
fi

for file in $*;
do 
  base=${file%%.*}
  echo "Converting $file to TIFF..."
  if [[ "$OSTYPE" == "darwin"* ]]; then
    # MacOS
    sips -s format tiff -s formatOptions lzw -s dpiWidth 300.0 -s dpiHeight 300.0 --resampleWidth 1200 $file --out $base.tif
  elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Ubuntu and other Linux distros
    #  TODO Figure out why output TIFF is ~4X larger in Linux vs MacOS.
    #       1.8 MB vs. 400 KB for a typical Conklin dictionary page
    convert $file -density 300x300 -geometry 1200 -compress lzw $base.tif
  else
    echo "ERROR: This script does not yet support $OSTYPE"
    echo ""
    exit 1
  fi
done


