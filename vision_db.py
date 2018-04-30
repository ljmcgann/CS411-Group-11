"""TO RUN: must have this file and the apikey.json file in the same folder. 

!!!Then must write in command line: 'export GOOGLE_APPLICATION_CREDENTIALS=apikey.json'. 

This will output the safe_search api which is basically if the picture is violent, for adults, about injuries(medical)
and inappropriate context overall.


in terminal, as example, write following:

python visionex.py safe-search ./rick.jpg

notice that   ./rick.jpg    is the path of picture you want to use
"""

import argparse
import io
import os
from google.cloud import vision
from google.cloud.vision import types
import sys
from pymongo


def detect_safe_search(path):
    """Detects unsafe features in the file."""
    client = vision.ImageAnnotatorClient()
    
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.types.Image(content=content)

    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation
    
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    
    title = 'Safe search:'
    global search_a = 'adult: {}'.format(likelihood_name[safe.adult])
    global search_m = 'medical: {}'.format(likelihood_name[safe.medical])
    global search_s = 'spoofed: {}'.format(likelihood_name[safe.spoof])
    global search_v = 'violence: {}'.format(likelihood_name[safe.violence])
    print(title)
    print(search_a)
    print(search_m)
    print(search_s)
    print(search_v)


def run_local(args):
    if args.command == 'safe-search':
        detect_safe_search(args.path)

def calculateScore(result):
    if result == "UNKNOWN":
        return 0
    elif result == "VERY_UNLIKELY":
        return -2
    elif result == "UNLIKELY":
        return -1
    elif result == "POSSIBLE":
        return 0.5
    elif result == "LIKELY":
        return 2
    elif result == "VERY_LIKELY":
        return 5

def run_database(username):
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    db = client.test_database

    users = db['users']

    if users.find({'username':username}) == None:
        user = {}
        user['username'] = username
        user['adult_score'] = calculateScore(search_a)
        user['medical_score'] = calculateScore(search_m)
        user['spoof_score'] = calculateScore(search_s)
        user['violence_score'] = calculateScore(search_v)
        users.insert(user)
    else:
        result = users.find({'username':username})
        adult_score = users.result[0]['adult_score']
        medical_score = users.result[0]['medical_score']
        spoof_score = users.result[0]['spoof_score']
        violence_score = users.result[0]['violence_score']

        user = {}
        user['username'] = username
        user['adult_score'] = adult_score + calculateScore(search_a)
        user['medical_score'] = medical_score + calculateScore(search_m)
        user['spoof_score'] = spoof_score + calculateScore(search_s)
        user['violence_score'] = violence_score + calculateScore(search_v)
        users.update({'username':username},{$set:user})



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                                     description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')

    safe_search_parser = subparsers.add_parser(
                                               'safe-search', help=detect_safe_search.__doc__)
    safe_search_parser.add_argument('path')

    args = parser.parse_args()
    run_local(args)


    run_database(username)







