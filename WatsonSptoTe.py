# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:34:48 2017

@author: Nitin Kishore Sai Samala
"""

# Using IBM Watson Speech to Text API.

import json
from watson_developer_cloud import SpeechToTextV1


UNAME = "d5e0bb24-924d-4d2f-89c2-0b48a6c86a32"
PWD = "OM1zJUbkq3iw"

sptote = SpeechToTextV1(username=UNAME, password=PWD)

# Filename of the selected audio file
audio_file = open("rapgod.ogg", "rb")
print "Processing Audio (Speech)"

# Transcribing
with open('text_result_.json', 'w') as fp:
    result = sptote.recognize(audio_file, content_type="audio/ogg",
                           continuous=True, timestamps=False,
                           max_alternatives=1)
    print result
    json.dump(result, fp, indent=2)
    
print "Conversion to text, complete"