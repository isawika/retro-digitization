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
  sips -s format tiff -s formatOptions lzw -s dpiWidth 300.0 -s dpiHeight 300.0 --resampleWidth 1200 $file --out $base.tif 
done



