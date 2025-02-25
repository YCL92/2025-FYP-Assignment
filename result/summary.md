# Projects in Data Science (2025)
## Introduction - Malik
Cancer is a global problem affecting millions of people every year, in 2022 approximately 20 million people worldwide were diagnosed with cancer, and 9.7 million people died from various cancers. [[1]](#1)

One of the leading causes of cancer in Europe is melanoma (#7 in 2022) [[2]](#2), which is a type of skin cancer, and is generally considered the most dangerous type of skin cancer due to having the highest mortality rate among all skin cancers, while melanoma only appears in 1% of all skin cancer diagnoses. [[3]](#3)

Due to melanoma being one of the leading causes of cancer in Europe, and the mortality rate of melanoma being relatively high compared to other types of skin cancer, it is very important to have good diagnostical methods available in order to catch melanoma as early as possible, such that the survival rate increases for people diagnosed with melanoma.

That is where this project comes into play, where machine learning techniques will be applied. This is done in order to analyze a series of skin lesion images, such that a good tool can be created for detecting melanoma, and ultimately help further develop tools such as this one, which can be used to prevent future cases of melanoma. 

For this part of the assignment, the primary focus is on the hair removal techniques used in order to get clearer images of the skin lesions themselves, and therefore no detection of melanoma happens during this part.

## Strategy development - Gabi

To analyze skin lesion features accurately, we need to remove hair from the images, as it obstructs the lesions and affects feature analysis. To achieve this, we first reviewed all 200 skin lesion images and identified the types of image enhancements required for effective hair removal. This step is crucial because hair removal tools perform better when hairs are more distinguishable. Moreover, the picture enhancement techniques help to better visualize skin lesion itself for better features detection. 

After manually analyzing the images, we present the following examples from our dataset that require image enhancement. Additionally, we specify the type of enhancement that can be applied to improve hair visibility for more efficient removal and lesion feature detection.

### Example pictures:

1. ![image](https://github.com/user-attachments/assets/1e943f0d-2b36-4560-b7c9-f3502d4cfb93)
2. ![image](https://github.com/user-attachments/assets/6abab688-35b6-4eea-973f-2b19ae1a6d4e)
3. ![image](https://github.com/user-attachments/assets/5e9a09b8-135e-42eb-a488-f03f45e7852e)
4. ![image](https://github.com/user-attachments/assets/6fd047a4-bef8-4726-ad82-ca2798b8a250)

Isues represented in example pictures that interfier with hair removal:
1. Blurryness
2. Noise
3. White hair (makes harder to segment hair)
4. Low contrast images

## References
<a id="1">[1]</a> National Cancer Institute (2024). 
<a href="https://www.cancer.gov/about-cancer/understanding/statistics">Cancer Statistics</a>.\
<a id="2">[2]</a> World Health Organization (WHO), Global Cancer Observatory. (2024). 
<a href="https://gco.iarc.who.int/media/globocan/factsheets/populations/908-europe-fact-sheet.pdf">Cancer Today (Globocan 2022)</a>.\
<a id="3">[3]</a> National Cancer Institute (2024). 
<a href="https://www.cancer.gov/types/skin/hp/melanoma-treatment-pdq">Melanoma Treatment (PDQ®) – Health Professional Version</a>.







