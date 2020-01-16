import json
import datetime
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

json_open = open ('test_wave.json')  
data = json.load(json_open)
json_open.close()
number_of_waves = 0

sub_string = "waved hello to the group."

for messages in data['messages']:
    try:
        message = messages['content']
        if sub_string in message:
            number_of_waves += 1
    except:
        continue
print (number_of_waves)