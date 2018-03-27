"""TO RUN: must have this file and the apikey.json file in the same folder. 

Then must write in command line: 'export GOOGLE_APPLICATION_CREDENTIALS=apikey.json'. 

Then to run you have to download a picture into the folder and then add the picture name as an argument...
python visionex.py pictureName          

This will output the safe_search api which is basically if the picture is violent, for adults, about injuries(medical)
and inappropriate context overall. 

The code i have commented out is to use the labels api which just describes what 
is shown in the picture with basic labels (nothing to do with violence but very descriptive). 

"""



import io
import os
from google.cloud import vision
from google.cloud.vision import types
import sys
images = [sys.argv[1]]
#print sys.argv[1]
vision_client = vision.ImageAnnotatorClient()
#images = ['war_tank.jpg', 'isis.jpg', 'bleedingman.jpg']
#images = ['Selena_Gomez_-_Walmart_Soundcheck_Concert.jpg', 'selena2.jpg', 'selena3.jpg', 'selena4.jpg', 'selena5.jpg', 'selenagomez.jpg']

for x in images:
    with io.open(x, 'rb') as image:
        content = image.read()
        image = types.Image(content=content)

	#response = vision_client.label_detection(image=image)
    #labels = response.label_annotations
    response = vision_client.safe_search_detection(image=image)
    labels = response.safe_search_annotation
    print labels
    #for label in labels:
    #print label.description #, label.score
