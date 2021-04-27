# How to Digitize a Historical Dictionary

## 2. Text Capture

Once you have a PDF version of the document, you would use an Optical Character Recognition (OCR) software to convert it into plain text. We recommend using [Tesseract](https://github.com/tesseract-ocr/tesseract) because besides being open-source with a large user community (whom you can ask for help), it supports over XXX languages so there's a fair chance it can readily convert your document. More importantly, you can train Tesseract if none of the pre-built language models are good enough. You will do that next.

---
__Prerequisite:__ _Install Tesseract_

You need to compile the Tesseract source code in order to use the training tools.

- [Download](https://github.com/tesseract-ocr/tesseract/releases) and uncompress the source of the latest release (e.g., "v4.1.1")
- Rename the folder 
```
$ mv tesseract-4.1.1 tesseract
```

- Run the following commands from a console. The programs will be installed in the folder _/usr/local/bin_

```
$ cd tesseract
$ ./configure
$ make
$ make training
$ sudo make install training-install
```

NOTE:  If the _./configure_ command gives "undefined M4 macro" errors, run the command "_autoreconf --install_" first and then run "_./configure_" again.

---

### 2.1 Split the PDF document into separate pages

Split the pages so we use them individually and convert them to TIFF image files. (Tesseract doesn't read PDF pages.) 

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