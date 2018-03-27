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
