# How to Digitize a Historical Dictionary


Retro-digitization is the process of converting a paper-based historical publication into an electronic format suitable for publishing online or for sharing as a digital resource. In this tutorial, you will learn the workflow we developed to digitize a 1953 bilingual dictionary. For details, see our paper *"Using Open-Source Tools to Digitize Lexical Resources for Low-Resource Languages"* (upcoming).

We designed the workflow to enable even those with modest budgets to conduct their own retro-digitization projects. In doing so, we hope to encourage more communities, especially speakers of minority and indigenous languages, to build e-dictionaries and other digital lexical resources for their mother-tongue language.

## What You'll Do

You will use sample pages from Harold Conklin's Hanunoo-English dictionary. Hanunoo (IPA: "hanunuʔɔ") is an indigenous language spoken by ~25,000 Hanunoo Mangyan people in the Philippines. Although they have a native writing system called [Surat Mangyan](https://en.wikipedia.org/wiki/Hanunuo_script), the dictionary itself had Hanunoo words printed in Roman letters plus two special characters: ŋ (eng) and ʔ (glottal stop).

You will train an OCR engine to recognize the special character 'ŋ' since no existing engine can (the glottal stop symbol will be handled differently). You will also format the OCR-ed pages into XML then load/edit/display them in a locally-installed [Lexonomy](https://www.lexonomy.eu/) dictionary server. How cool is that? :-)

![Example Lexonomy dictionary](./images/lexonomy-entry.png)
_Example dictionary hosted in Lexonomy_

## Prerequisites

1. Computer running Ubuntu 18.04 or later (see Note below)
2. Python 3 installed
3. Admin privilege to install software
4. You know how to run commands in a console

To follow along, first make sure you have copied this Git project into your home folder:
```
$ cd ~
$ git clone https://github.com/isawika/retro-digitization.git
$ cd retro-digitization
```

> Note: The tutorial should run on other Linux systems with only minor tweaks, but we have not tested. Running on Mac or Windows should also be possible but needs more work. Contact us if you want to discuss.  

## The Workflow

- [Step 1](./Step1-ImageCapture.md): Image Capture
- [Step 2](./Step2-TextCapture.md): Text Capture
- [Step 3](./Step3-Proofread.md): Proofread the transcriptions
- [Step 4](./Step4-CovertToXml.md): Convert to XML
- [Step 5](./Step5-Publish.md): Publish

