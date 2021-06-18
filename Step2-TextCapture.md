# How to Digitize a Historical Dictionary

## 2. Text Capture

Now that you have a PDF version of the dictionary, you will convert its pages into plain text. However it's common for historical dictionaries to be typeset in obsolete fonts or use special character symbols that are unknown to today's OCR software. If you use an OCR as-is, you will likely get lots of transcription errors that are too time-consuming and costly to correct. Thus it is better to first train the OCR to accurately recognize the dictionary's distinct typography. Fortunately, OCR tools such as [Tesseract](https://github.com/tesseract-ocr/tesseract) are trainable and will serve our purpose well.

To train the OCR, you:

 - select several pages (or more precisely, text regions in the pages) from the dictionary that provide good examples of special characters and/or fonts you want the OCR to recognize
 - manually create accurate transcriptions for the text regions you selected
 - feed the set of text + transcription pairs into Tesseract
 - wait until the training is complete

Let's begin!

---
__Prerequisite 1:__ &nbsp;_Install Tesseract_

You need to compile the Tesseract source code in order to use the training tools. The pre-built binaries unfortunately do not include them.

- [Download](https://github.com/tesseract-ocr/tesseract/releases) and uncompress the source of the latest release (e.g., "v4.1.1") in your home folder
- Rename the folder (for convenience)
```
$ mv tesseract-4.1.1 tesseract
```

- Run the following commands from a console. The programs will be installed in the folder _/usr/local/bin_

```
$ cd ~/tesseract
$ ./configure
$ make
$ make training
$ sudo make install training-install
```

> NOTE: If the _./configure_ command gives "undefined M4 macro" errors, run "_autoreconf --install_" first and then run "_./configure_" again.

__Prerequisite 2:__ &nbsp;_Install PDFtk and ImageMagick_

_PDFtk_ is a handy tool for splitting/joining/rotating PDF files while _ImageMagick_ converts PDF files into TIFF and provides lots of image processing features. 

```
$ sudo apt install pdftk-java
$ sudo apt install imagemagick
```

Edit the ImageMagick policy _/etc/ImageMagick-6/policy.xml_ to allow converting PDF files. Look for a line like below and set value of __rights__ to "read | write":

`<policy domain="coder" rights="read | write" pattern="PDF" />`

---

### 2.1 Split the PDF document and convert the pages to TIFF images

```
$ cd ~/retro-digitization/tutorial
$ pdftk ConklinSample.pdf burst output train-%02d.pdf
$ ../pdf2tiff.sh train*.pdf
```

You should see 3 TIFF files named _train-01.tif, train-02.tif, train-03.tif_

### 2.1 Prepare the OCR training data



  - select training pages
  - create Tesseract box files

### 2.2 Train the OCR engine

Tesseract supports three options for training its neural network-based recognition engine: 1) Fine tune, 2) Retrain the top layer or 3) Retrain from scratch. We will use the first option because it requires less effort and frankly, the OCR can accurately recognize the scanned pages except the few special characters. Fine tuning may also be a good option if you simply need the OCR to recognize a new set of fonts for a given language.

### 2.3 Transcribe the dictionary pages

## Preparation

complexity
novel characters
book layout
dictionary microstructure


<br/>

[Step 3](./Step3-Proofread.md) - Proofread the transcriptions