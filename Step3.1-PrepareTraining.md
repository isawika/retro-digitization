# How to Digitize a Historical Dictionary

### 3.1 - Prepare the Training Data

#### 3.1.1 Split the PDF document and convert the pages to TIFF images

```
$ cd WORKDIR/retro-digitization/tutorial
$ pdftk ConklinSample.pdf burst output sample-%02d.pdf
$ ../pdf2tiff.sh sample*.pdf
```

For your actual project, __pdftk__ will produce as many split PDF files as the number of pages in your dictionary. In this tutorial, we made only 5 pages of the Conklin dictionary available so you should see TIFF files named _sample-01.tif, ..., sample-05.tif_

#### 3.1.2 Select the training text

> Note: In our paper, we described using the JTessBox tool to create Box files for training Tesseract. We since learned that this is not needed; we show a simpler way below.  



---
<br/>

[Step 3.2](./Step3.2-Finetune.md) - Finetune Tesseract