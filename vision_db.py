"""TO RUN: must have this file and the apikey.json file in the same folder. 

Then must write in command line: 'export GOOGLE_APPLICATION_CREDENTIALS=apikey.json'. 

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
    print('Safe search:')
    print('adult: {}'.format(likelihood_name[safe.adult]))
    print('medical: {}'.format(likelihood_name[safe.medical]))
    print('spoofed: {}'.format(likelihood_name[safe.spoof]))
    print('violence: {}'.format(likelihood_name[safe.violence]))


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

def run_database(username, adult, medical, spoof, violence):
    client = pymongo.MongoClient('mongodb://localhost:27017/')

    db = client.test_database

    users = db['users']

    if users.find({'username':username}) == None:
        user = {}
        user['username'] = username
        user['adult_score'] = calculateScore(adult)
        user['medical_score'] = calculateScore(medical)
        user['spoof_score'] = calculateScore(spoof)
        user['violence_score'] = calculateScore(violence)
        users.insert(user)
    else:
        adult_score = users.
        medical_score = users.
        spoof_score = users.
        violence_score = users.

        user = {}
        user['username'] = username
        user['adult_score'] = adult_score + calculateScore(adult)
        user['medical_score'] = medical_score + calculateScore(medical)
        user['spoof_score'] = spoof_score + calculateScore(spoof)
        user['violence_score'] = violence_score + calculateScore(violence)
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

    run_database()








