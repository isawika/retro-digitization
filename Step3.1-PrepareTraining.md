# How to Digitize a Historical Dictionary

### 3.1 - Prepare the Training Data

#### 3.1.1 Split the PDF document and convert the pages to TIFF images

```
$ cd retro-digitization/tutorial
$ pdftk ConklinSample.pdf burst output sample-%02d.pdf
$ ../pdf2tiff.sh sample*.pdf
```

For your actual project, __pdftk__ will produce as many split PDF files as the number of pages in your dictionary. In this tutorial, we made only 5 pages of the Conklin dictionary available so you should see TIFF files named _sample-01.tif, ..., sample-05.tif_

#### 3.1.2 Choose the Pre-trained Language Model

The goal is to find a Tesseract language model that does the best job of transcribing the dictionary. You may need to try several models, but you can dramatically cut down the possibilies using some informed guesswork.

Download the Spanish and English language models.

> Note: Even if you're not using the English language to OCR, it is needed to avoid the Tesseract warning message.

```
$ cd retro-digitization/tutorial
$ mkdir tessdata
$ wget -P ./tessdata https://github.com/tesseract-ocr/tessdata_best/raw/master/spa.traineddata
$ wget ./tessdata https://github.com/tesseract-ocr/tessdata_best/raw/master/eng.traineddata
```

OCR the sample pages using the Spanish model.

```
$ export TESSDATA_PREFIX=./tessdata
$ ../runocr.sh *.tif -l spa
```

You should see 5 OCR-ed pages named sample-01.txt, ..., sample-05.txt

> Note: For Conklin's dictionary we tried:
> 1. __English__ - since the dictionary is bilingual
> 2. __Tagalog__ - being a Philippine language like Hanunoo
> 3. __Spanish__ - Spain introduced the [Spanish alphabet](https://en.wikipedia.org/wiki/Filipino_orthography) when they colonized the Philippines
> 4. __Old Spanish__ - seems especially relevant
>
> We used each model to OCR a set of test pages and chose the Spanish model, as it performed the best in transcribing vowels with diacritical marks. However, none could recognize the eng 'ŋ' and glottal stop 'ʔ' symbols.

__Optional__

Download and experiment with the Tagalog and Old Spanish language models. Compare their OCR accuracy against the Spanish model's. 

```
# Tagalog has no 'best LSTM' model, so download the standard one
$ wget -P ./tessdata https://github.com/tesseract-ocr/tessdata/raw/master/tgl.traineddata

$ wget ./tessdata https://github.com/tesseract-ocr/tessdata_best/raw/master/spa_old.traineddata
```

Before rerunning the __runocr.sh__, move or rename the previously OCR-ed text files or else they will be overwritten.

#### 3.1.2 Select the training text

> Note: In our paper, we described using the JTessBox tool to create Box files for training Tesseract. We since learned that this is not needed; we show a simpler way below.  

This substep is more art than science. Your goal is to select a representative sample of the dictionary text from which Tesseract will learn how to recognize the new characters. While it's not possible to give exact instructions, we offer these guidelines:

- Choose entries from different pages in the dictionary. Ideally you want to sample widely and not just from say, the first few pages.
- Choose text where the special characters occur in a variety of positions (start, middle and end of words)
- You don't need many examples. Perhaps 25-50 lines for each special character may be enough.

Open the OCR-ed pages of your chosen training text and manually correct the OCR errors. That is, replace the misrecognized characters with the actual special symbols.

Copy the all training text into a single text file, removing any blank lines.

Below is the training text we choose to fine-tune Tesseract to recognize the Hanunoo and English words in Conklin's dictionary. Notice it's only 40 lines long.

- [hanunoo.txt](./tutorial/hanunoo.txt)

We ran a handful of experiments to ultimately come up with this training data. There's nothing special about it; one can find other text in the dictionary that could produce a similar (or even better) performing language model. But we found it was good enough to achieve 98-99% OCR accuracy.

---
<br/>

[Step 3.2](./Step3.2-Finetune.md) - Finetune Tesseract