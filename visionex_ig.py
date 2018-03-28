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
import instagram_test as ig

def test_with_ig():
    images = ig.get_image_bytes()
    vision_client = vision.ImageAnnotatorClient()

    for img_bytes in images:
        image = types.Image(content=img_bytes)
        vision_client = vision.ImageAnnotatorClient()
    	#response = vision_client.label_detection(image=image)
        #labels = response.label_annotations
        response = vision_client.safe_search_detection(image=image)
        labels = response.safe_search_annotation
        print labels
        #for label in labels:
        #print label.description #, label.score

test_with_ig()
