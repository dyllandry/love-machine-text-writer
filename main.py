import json
import os
import sys
import random
import string
from datetime import datetime

def getRandomString(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def getUid():
    return getRandomString(10)

if  len(sys.argv) != 2:
    print("Usage: python3 main.py \"<text>\"")
    sys.exit(1)

# could write this dict as one declaration
smsData = {
        'messageId': getUid(),
        'createdAt': datetime.isoformat(datetime.utcnow()),
        'text': sys.argv[1]
}

dataToWrite = []

try:
    # If file exists, grab its existing data then delete it.
    file = open('out.json', 'r+')
    fileContent = file.read()
    if (len(fileContent) > 0):
        existingData = json.loads(fileContent)
        for data in existingData: dataToWrite.append(data) 
        # Erase data
        file.close()
        open('out.json', 'w').close()
except IOError:
    # If file doesn't exist, create it
    open('out.json', 'w').close()

# Open file & write data
file = open('out.json', 'r+')
dataToWrite.append(smsData)
json.dump(dataToWrite, file)
file.close()

