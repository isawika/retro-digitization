# How to Retro-Digitize a Historical Dictionary

## Step 3.3: Transcribe the Dictionary Pages

Use the trained Hanunoo model to OCR the dictionary. For this tutorial, you will OCR the same 5 sample pages.

```
cd retro-digitization/tutorial
export TESSDATA_PREFIX=./final

tesseract sample-01.tif trained-01 -l hnn
tesseract sample-02.tif trained-02 -l hnn
tesseract sample-03.tif trained-03 -l hnn
tesseract sample-04.tif trained-04 -l hnn
tesseract sample-05.tif trained-05 -l hnn
```

You should see 5 OCR-ed text files: _trained-01.txt, ... trained-05.txt_

<br/>

[Step 4](./Step3.4-Proofread.md) - Proofread
