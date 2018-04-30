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

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "instasafe/apikey.json"

def get_user_data(access_token):
    i = 0
    res = []
    (urls, images) = ig.get_image_bytes(access_token)
    vision_client = vision.ImageAnnotatorClient()
    #vision_client = vision.ImageAnnotatorClient().from_service_account_json('apikey.json')

    res = [ [u, None] for u in urls]
    for img_bytes in images:
        image = types.Image(content=img_bytes)
        vision_client = vision.ImageAnnotatorClient()
    	#response = vision_client.label_detection(image=image)
        #labels = response.label_annotations
        response = vision_client.safe_search_detection(image=image)
        labels = response.safe_search_annotation
        res[i][1] = labels
        print labels
        i += 1
        #for label in labels:
        #print label.description #, label.score
    return toHTMLDict(res)

def toHTMLDict(res):
    dicto = {}
    x = 0
    for i in res:
        #(arg1, arg2) = res[x]
        arg1 = res[x][0]
        arg2 = res[x][1]
        first = 'url'+ str(x)
        second = 'label'+ str(x)
        dicto[first] = arg1
        dicto[second] = arg2
        x += 1
    return dicto
