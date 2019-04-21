import cv2
from pickle import dump, HIGHEST_PROTOCOL, load
import sys
from deepdiff import DeepDiff
import json
orb = cv2.ORB_create(nfeatures=100000, scoreType=cv2.ORB_FAST_SCORE)

areaMap = cv2.imread("images/Map1.jpg")
areaMap = cv2.resize(areaMap, (0, 0), fx = 0.5, fy = 0.5)
areaMap = cv2.cvtColor(areaMap, cv2.COLOR_BGR2GRAY)

# find the keypoints and descriptors with ORB
keys, descs = orb.detectAndCompute(areaMap, None)

with open('keys', 'wb') as output:  # Overwrites any existing file.
    ob = (map(lambda x: {'pt': x.pt, 'size': x.size, 'angle': x.angle, 'response': x.response, 'octave': x.octave, 'class_id': x.class_id}, keys))
    dump(ob, output, HIGHEST_PROTOCOL)
    print('dumped keys to \'keys\'')
    output.close()

with open('descs', 'wb') as output:  # Overwrites any existing file.
    dump(descs, output, HIGHEST_PROTOCOL)

    print('dumped keys to \'descs\'')
