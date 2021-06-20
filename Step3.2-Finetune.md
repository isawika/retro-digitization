# How to Digitize a Historical Dictionary

### 3.2 Finetune the OCR engine

Tesseract supports three options for training its neural network-based recognition engine: 1) Fine tune, 2) Retrain the top layer or 3) Retrain from scratch. We will use the first option because it requires less effort and frankly, the OCR can accurately recognize the scanned pages except the few special characters. Fine tuning may also be a good option if you simply need the OCR to recognize a new set of fonts for a given language.

To train the OCR, you:

 - select several pages (or more precisely, text regions in the pages) from the dictionary that provide good examples of special characters and/or fonts you want the OCR to recognize
 - manually create accurate transcriptions for the text regions you selected
 - train Tesseract so that it recognizes the new characters in the transcriptions
 
<br/>

[Step 3.3](./Step3.3-Proofread.md) - Create the Transcriptions & Proofread