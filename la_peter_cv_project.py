# -*- coding: utf-8 -*-
"""La_Peter_CV_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16xl8U7AlA4qi1zEuPnm_JEoJlLrIk_2q

MSDS692 Data Science Practicum - Computer Vision

Author: Peter La

Title: Build My Own ‘Google Translate’ for Food Menus in Vietnamese

Date: March 10, 2025

Purpose: Use OCR to identify the Vietnamese words in images.

Input: images of Vietnamese menus

Outputs: OCR identifies Vietnamese words
"""

!apt-get update
!apt-get install -y tesseract-ocr
!apt-get install -y tesseract-ocr-vie
!pip install pytesseract pillow

import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

def process_an_image(image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="vie")
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        axes[0].imshow(image)
        axes[0].axis("off")
        axes[0].set_title("Original Image")
        axes[1].text(0, 1, text, fontsize=12, verticalalignment='top', wrap=True)
        axes[1].axis("off")
        axes[1].set_title("OCR Output")
        return fig

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
dpi = 300

from google.colab import drive
drive.mount('/content/drive')

path = '/content/drive/MyDrive/cv_data/output/'

fig = process_an_image('/content/drive/MyDrive/cv_data/vtest1.png')
output_filename = 'output1.png'
fig.savefig(path + output_filename, dpi=dpi)

fig = process_an_image('/content/drive/MyDrive/cv_data/vtest2.jpg')
output_filename = 'output2.png'
fig.savefig(path + output_filename, dpi=dpi)

fig = process_an_image('/content/drive/MyDrive/cv_data/vtest3.jpg')
output_filename = 'output3.png'
fig.savefig(path + output_filename, dpi=dpi)

fig = process_an_image('/content/drive/MyDrive/cv_data/vtest4.png')
output_filename = 'output4.png'
fig.savefig(path + output_filename, dpi=dpi)

fig = process_an_image('/content/drive/MyDrive/cv_data/vtest5.png')
output_filename = 'output5.png'
fig.savefig(path + output_filename, dpi=dpi)

fig = process_an_image('/content/drive/MyDrive/cv_data/menu1.jpg')
output_filename = 'output6.png'
fig.savefig(path + output_filename, dpi=dpi)

fig = process_an_image('/content/drive/MyDrive/cv_data/menu2.png')
output_filename = 'output7.png'
fig.savefig(path + output_filename, dpi=dpi)

fig = process_an_image('/content/drive/MyDrive/cv_data/menu3.jpg')
output_filename = 'output8.png'
fig.savefig(path + output_filename, dpi=dpi)