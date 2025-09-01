# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:49:27 2021

@authors: Md. Farhadul Islam & Sarah Zabeen
"""

from easygui import *
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import sys

detection = load_model('auto_chloro_model.h5')

# message to be displayed  
text = 'Welcome, dear user\
\nTo know about your crop (leaf type) diseases and their remedies, please take a picture of the leaf\
\nand click on the *Select Image* button to upload that image.'

# show logo
img = "auto-chloro.PNG"

# window title 
title = "File Open-Path"
  
# button list 
button_list = [] 
  
button1 = "Select Image"
button2 = "Close"

button_list.append(button1) 
button_list.append(button2)

# creating a button box 
output = buttonbox(msg=text, title=title, image=img, choices=button_list) 

if output == 'Select Image':
    txt = ''
    path = fileopenbox()
    pred = buttonbox(msg="Click on the image to detect the disease", title='Detection', image=path, choices=('Cancel',)) 
    if pred != path:
        sys.exit()
        
    test_img = image.load_img(path, target_size=(48,48))
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0) 
    result = detection.predict(test_img)
    a = result.argmax()
    classes = [
        'Pepper__bell___Bacterial_spot images',
        'Pepper__bell___healthy images',
        'Potato___Early_blight images',
        'Potato___healthy images',
        'Potato___Late_blight images',
        'Tomato_Bacterial_spot images',
        'Tomato_Early_blight images',
        'Tomato_healthy images',
        'Tomato_Late_blight images',
        'Tomato_Leaf_Mold images',
        'Tomato_Septoria_leaf_spot images',
        'Tomato_Spider_mites_Two_spotted_spider_mite images',
        'Tomato__Target_Spot images',
        'Tomato__Tomato_mosaic_virus images',
        'Tomato__Tomato_YellowLeaf__Curl_Virus images'
    ]
    category = []
    for i in classes:
        category.append(i)
    for i in range(len(classes)):
        if i == a:
            output = category[i]

    if output == 'Pepper__bell___Bacterial_spot images':
        output = 'Bell Pepper Bacterial Spot Disease'
        txt = 'Biological control:\n\nControl of bacterial spot is very difficult and expensive. \
If the disease appears early in the season, it is better to destroy the entire crop. \
Copper-based bactericides create a protective coating on fruits and foliage. \
Bacteriophages (viruses that kill bacteria) are available on the market which kill specific bacteria. \
Soak seeds in 1.3% sodium hypochlorite solution for 1 minute or in hot water (50°C) for 25 minutes. \
\n\nChemical control:\n\nAlways try to use integrated pest management (IPM). \
Using only copper-based bactericides can prevent and partially control the disease. \
Spraying should be done at the first appearance of symptoms, and repeated every 10–14 days in warm, humid weather. \
Mixtures of mancozeb and copper-based fungicides may provide better protection.'

    elif output == 'Potato___Early_blight images':
        output = 'Potato Early Blight Disease'
        txt = 'Biological control:\n\nBacillus subtilis-based formulations or copper-based \
organic fungicides are approved for use against this disease. \
\n\nChemical control:\n\nUse integrated pest management with biological control. \
Many fungicides are available in the market to control early blight. \
Fungicides such as azoxystrobin, pyraclostrobin, difenoconazole, boscalid, chlorothalonil, fenamidone, maneb, mancozeb, trifloxystrobin, \
and ziram can be used. Rotating different fungicide groups is recommended. Ensure timely crop management during favorable weather. \
Leave a pre-harvest interval after fungicide application to ensure food safety.'

    elif output == 'Potato___Late_blight images':
        output = 'Potato Late Blight Disease'
        txt = 'Biological control:\n\nApply copper-based fungicides before the onset of humid weather. \
Spraying organic protective coatings on leaves may also help prevent infection. \
\n\nChemical control:\n\nUse integrated pest management. Fungicides must be used in fields, especially in humid areas, to control late blight. \
Protective fungicides that coat leaves are effective when applied preventively. \
Fungicides such as mandipropamid, chlorothalonil, fluazinam, triphenyltin, or mancozeb can be applied. \
Seed treatment with fungicides such as mancozeb before planting is also effective.'

    elif output == 'Tomato_Bacterial_spot images':
        output = 'Tomato Bacterial Spot Disease'
        txt = 'Biological control:\n\nVery difficult and costly to manage. \
If infection occurs early in the season, destroy the crop. Copper-based bactericides are used preventively. \
Bacteriophages (viruses that kill bacteria) are available. \
Soaking seeds in 1.3% sodium hypochlorite for 1 min or in hot water (50°C) for 25 min reduces infection. \
\n\nChemical control:\n\nUse copper-based bactericides preventively. \
Spray at the first symptoms and repeat every 10–14 days in warm, humid weather. \
Due to resistance, it is recommended to mix copper bactericides with mancozeb.'

    elif output == 'Tomato_Early_blight images':
        output = 'Tomato Early Blight Disease'
        txt = 'Biological control:\n\nBacillus subtilis-based formulations or copper-based \
organic fungicides can be used. \
\n\nChemical control:\n\nFungicides such as azoxystrobin, pyraclostrobin, difenoconazole, boscalid, chlorothalonil, fenamidone, maneb, mancozeb, trifloxystrobin, \
and ziram are effective. Rotate fungicide groups to prevent resistance. Follow timely cultural practices and allow a safe pre-harvest interval.'

    elif output == 'Tomato_Late_blight images':
        output = 'Tomato Late Blight Disease'
        txt = 'Biological control:\n\nNo effective biological measures reported. \
Remove and destroy infected plants immediately and avoid using them for compost. \
\n\nChemical control:\n\nPreventive spraying with mandipropamid, chlorothalonil, fluazinam, or mancozeb is recommended. \
Apply during wet seasons or heavy rainfall.'

    elif output == 'Tomato_Leaf_Mold images':
        output = 'Tomato Leaf Mold Disease'
        txt = 'Biological control:\n\nSeed treatment with hot water (50°C for 25 min). \
Use beneficial fungi such as Trichoderma harzianum, Trichoderma viride, or others as biocontrol agents. \
Home remedies like apple cider vinegar, garlic extract, or milk mixtures can also help. \
\n\nChemical control:\n\nApply fungicides preventively when conditions are favorable. \
Chlorothalonil, maneb, mancozeb, and copper-based fungicides are recommended. \
For greenhouses, fungicides like difenoconazole, mandipropamid, cymoxanil, famoxadone, and cyprodinil are advised.'

    elif output == 'Tomato_Septoria_leaf_spot images':
        output = 'Tomato Septoria Leaf Spot Disease'
        txt = 'Biological control:\n\nCopper fungicides such as Bordeaux mixture, copper hydroxide, copper sulfate, \
or copper oxychloride can help. Spray every 7–10 days during flowering and fruiting. \
\n\nChemical control:\n\nFungicides such as maneb, mancozeb, and chlorothalonil are effective. \
Spray every 7–10 days during flowering and fruiting.'

    elif output == 'Tomato_Spider_mites_Two_spotted_spider_mite images':
        output = 'Spider Mite Infestation'
        txt = 'Biological control:\n\nWash leaves with water and remove infested leaves. \
Neem oil, garlic tea, stinging nettle extract, or insecticidal soap can be sprayed. \
Introduce predatory mites (e.g., Phytoseiulus persimilis) or use biopesticides like Bacillus thuringiensis. \
Repeat spraying after 2–3 days. \
\n\nChemical control:\n\nDifficult to manage with chemicals due to resistance. \
If necessary, use sulfur (3 g/L), spiromesifen (1 ml/L), dicofol (5 ml/L), or abamectin carefully. \
Repeat spraying after 2–3 days.'

    elif output == 'Tomato__Target_Spot images':
        output = 'Tomato Target Spot Disease'
        txt = 'Water plants in the morning so leaves dry quickly. \
Use drip irrigation to avoid wetting leaves. Apply mulch to prevent fruit from touching the soil.'

    elif output == 'Tomato__Tomato_mosaic_virus images':
        output = 'Tomato Mosaic Virus Disease'
        txt = 'Biological control:\n\nSeed treatment by dry heat (70°C for 4 days or 82–85°C for 24 hours) or soaking in 10% trisodium phosphate solution for 15 min. \
\n\nChemical control:\n\nNo effective chemical control is available for this virus.'

    elif output == 'Tomato__Tomato_YellowLeaf__Curl_Virus images':
        output = 'Tomato Yellow Leaf Curl Virus Disease'
        txt = 'Biological control:\n\nNo effective management is available. Control whitefly populations to avoid spread. \
\n\nChemical control:\n\nNo cure once plants are infected. Insecticides from the pyrethroid group can reduce whitefly populations, \
but overuse may cause resistance.'

    elif output in ['Pepper__bell___healthy images', 'Potato___healthy images', 'Tomato_healthy images']:
        output = 'Healthy'

    if output != 'Healthy':
        new = textbox(output, 'Detection', txt)
    else:
        new = msgbox(output, 'Detection', 'End')
    
elif output == img:
    new = msgbox("Auto Chloro is a machine learning software that detects plant diseases from images. \
It also provides remedies for the detected diseases.\
\n\nDeveloped by Farhad and Sarah.\
\nTeam Hydro AI - 2021",
               "About Us", "End")
