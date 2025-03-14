### Computer Vision - Vietnamese Menu OCR and Translation Model 

Title: Building My Own ‘Google Translate’ for menus in Vietnamese
<br/>Purpose: Use OCR to identify the Vietnamese words in images

### Project Overview
Ordering food in a Vietnamese restaurant with its menu only in Vietnamese can be a struggle, especially if you’re unfamiliar with the language. A study revealed specific accuracy rates for Google Translate across languages, including 94% for Spanish, 90% for Tagalog, 82.5% for Korean, 81.7% for Chinese, and 77.5% for Vietnamese (with the lowest accuracy rate).

This project aims to create a highly accurate and efficient model for character recognition in Vietnamese restaurant menus. To do so, I need to tap into pre-trained models with my dataset of Vietnamese menu images. By training the model, I aim to automate menu translations.

This project utilizes both Google Colab and Python to detect characters in input images (OCR), emphasizing image processing, analysis, and modern deep learning techniques. The ipynb files are uploaded to this repository.

### Project Summary 

Ordering food in restaurants without English menus can significantly challenge non-native speakers. While translation tools like Google Translate offer some assistance, their accuracy varies across languages, with Vietnamese being one of the least accurate at only 77.5%. To address this issue, this project aims to develop an Optical Character Recognition (OCR) model designed explicitly for Vietnamese restaurant menus, enabling more accurate and automated menu translations.  

The project follows a structured approach, starting with data collection. A curated dataset of Vietnamese menu images was compiled for training and validation. Data preprocessing was then applied to enhance text clarity, ensuring that the images were optimized for OCR recognition. The model was built using a combination of pre-trained OCR frameworks, such as Tesseract, and deep learning techniques to refine character recognition. In the near future, image processing techniques such as text detection, segmentation, and enhancement will be implemented to improve accuracy further.  

After training and testing, the model’s performance was evaluated, and findings revealed both strengths and limitations. Key challenges included handling Vietnamese diacritical marks, dealing with varying font styles in menus, and overcoming the limited availability of high-quality Vietnamese text datasets. Despite these setbacks, the project demonstrated promising results, with potential improvements through further fine-tuning.  

Next steps involve expanding the dataset to include a broader variety of Vietnamese menu formats, refining text post-processing techniques to correct OCR-generated errors, and deploying the model into a real-world application, such as a mobile app or web-based tool. Additionally, real-world testing in Vietnamese restaurants will be conducted to validate the model’s usability and effectiveness. By continuing to refine and enhance this system, the project aims to create a practical and efficient solution for restaurant-goers seeking seamless menu translations.

