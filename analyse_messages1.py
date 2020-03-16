#!/usr/bin/python

import sys
import json
import datetime
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) != 2:
    print("niste dobro prosledili .json file")
    sys.exit()

color = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

#open json file
json_open = open (sys.argv[1])
data = json.load(json_open)
json_open.close()
names = []
number_of_messages = []

value_array_person_one = []
value_array_person_two = []
date_array = []

#get names of people in chat and set messages counter (for one day) for each person to 0 and draw legend
for participants in data['participants']:
    names.append (participants['name'])
    number_of_messages.append (int (0))
    #print (participants['name'])

persons = []
for i in range (0,len(names)):
    persons.append([])

#set last day
timestamp= int (data['messages'][0]['timestamp_ms'])
full_prew_date = date.fromtimestamp(timestamp/1000.0)
prew_message_day = full_prew_date.day

#get first day
counter = len(data['messages'])
timestamp = int (data['messages'][counter-1]['timestamp_ms'])
full_first_day = date.fromtimestamp(timestamp/1000.0)
first_message_dat = full_first_day.day

#number of days / second index for persons matrix
counter = 0

#get number of messages for each person on same day
for messages in data['messages']:
    
    timestamp= messages['timestamp_ms']
    full_date = date.fromtimestamp(timestamp/1000.0)
    message_day = full_date.day
    

    if prew_message_day == message_day:
        for i in range(len(names)):
            if names[i] == messages['sender_name']:
                number_of_messages[i]+=1
    
    else:
        for j in range(len(names)):
            persons[j].append (number_of_messages[j])

        counter += 1

        date_array.append(full_prew_date.strftime("%Y-%m-%d"))

        full_prew_date = full_date
        prew_message_day = message_day
        
        #resetuj brojace uz imena
        for i in range(len(names)):
            number_of_messages[i]=0

        #zapisi kome pripada poslednja poruka tog dana (prva u json-u)
        for i in range(len(names)):
            if names[i] == messages['sender_name']:
                number_of_messages[i]+=1


date_array.append(full_prew_date.strftime("%Y-%m-%d"))

for j in range(len(names)):
    persons[j].append (number_of_messages[j])
counter += 1

fig, ax = plt.subplots()

index = np.arange(len(date_array))

bar_width = 0.35
opacity = 0.4

error_config = {'ecolor': '0.3'}

rects = []
for k in range(0,len(names)):
    rects.append (plt.bar(index + k * bar_width, persons[k], bar_width, alpha=opacity, color=color[k], error_kw=error_config, label=names[k]))

plt.xlabel('Dates')
plt.ylabel('Number of messages')
plt.title('Number of messages per day for each person in conversation')
plt.xticks(index + bar_width / 2, date_array)
plt.legend()

plt.tight_layout()
plt.show()

#save raw values
#with open('excel1.txt', 'w') as save_file:
#    for listitem in value_array_person_one:
#        save_file.write('%s\n' % listitem)
##    save_file.write('\n')
#with open('excel2.txt', 'w') as save_file:
#    for listitem in value_array_person_two:
#        save_file.write('%s\n' % listitem)
##    save_file.write('\n')
#with open('excel_date.txt', 'w') as save_file:
#    for listitem in date_array:
#        save_file.write('%s\n' % listitem)
