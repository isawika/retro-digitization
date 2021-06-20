#!/bin/bash

if [ "$#" -eq 0 ]
then
  echo "usage: $0 <TIFF-files> -l <LANGUAGE>"
  echo ""
  exit 1
fi

POSITIONAL=()
while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in
    -l)
      LANGUAGE="$2"
      shift # past argument
      shift
      ;;
    *)    # unknown option
      POSITIONAL+=("$1") # save it in an array for later
      shift # past argument
      ;;
  esac
done

set -- "${POSITIONAL[@]}" # restore positional parameters

for file in $*;
do 
  base=${file%%.*}
  echo "Running OCR on $file using language '$LANGUAGE'..."
  tesseract $file $base -l $LANGUAGE
done


