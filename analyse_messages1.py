import json
import datetime
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

color = ["red", "green", "white"]

#open json file
json_open = open ('test.json')
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
    print (participants['name'])

#set last day
timestamp= int (data['messages'][0]['timestamp_ms'])
full_prew_date = date.fromtimestamp(timestamp/1000.0)
prew_message_day = full_prew_date.day

#get first day
counter = len(data['messages'])
timestamp = int (data['messages'][counter-1]['timestamp_ms'])
full_first_day = date.fromtimestamp(timestamp/1000.0)
first_message_dat = full_first_day.day

#draw x and y axis
#plt.axis([full_first_day, full_prew_date, 0, 10]) 


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
        #nacrtaj tacke na grafiku (osim ako im je vrednost 0) i pocni novi brojac
        #for i in range(len(names)):
          #  if number_of_messages[i] != 0:
                #plt.scatter(full_prew_date, number_of_messages[i],s=30,c=color[i])
           #     plt.plot(full_date,number_of_messages[i])
           #     value_array_person_one
                
        #for i in range(len(names)):
            #value_array_persons[i].append (number_of_messages [i])
            #value_array_persons[i] = np.append(value_array_persons[i],number_of_messages[i])
        value_array_person_one.append(number_of_messages[0])
        value_array_person_two.append(number_of_messages[1])
        date_array.append(full_prew_date)

        full_prew_date = full_date
        prew_message_day = message_day
        
        #resetuj brojace uz imena
        for i in range(len(names)):
            number_of_messages[i]=0

        #zapisi kome pripada poslednja poruka tog dana (prva u json-u)
        #for i in range(len(names)):
         #   if names[i] == messages['sender_name']:
          #      number_of_messages[i]+=1

#draw last day
#for i in range(len(names)):
 #   if number_of_messages[i] != 0:
  #      plt.scatter(full_prew_date, number_of_messages[i],s=30,c=color[i])
#for i in range(len(names)):
    #value_array_persons[i].append (number_of_messages [i])
    #value_array_persons[i] = np.append(value_array_persons[i],number_of_messages[i])
date_array.append(full_prew_date)
value_array_person_one.append(number_of_messages[0])
value_array_person_two.append(number_of_messages[1])

#print (value_array_persons[1])
#for people_messages in number_of_messages:
  #  print (people_messages)
#for i in range(len(names)):
    #plt.legend(color[i],names[i])
#plt.legend( loc=2)

#plt.plot(date_array,value_array_person_one, linewidth = 3, color = 'red')
#plt.plot(date_array,value_array_person_two, linewidth = 3, color = 'blue')
#position_bar_x = []
#print (len(value_array_persons[0]))
#position_bar_x[0]=np.arange(len(value_array_persons[0]))
#for i in range(len(names)):
 #   position_bar_x [i] = [x + 0.25 for x in position_bar_x[i-1]]

#bar_width = 0.25
#for i in range(len(names)):
 #   plt.bar(position_bar_x[i], value_array_persons[i], color[i], width=bar_width,edgecolor = 'white', label=date_array[i])

#plt.legend
#plt.show()

with open('excel1.txt', 'w') as save_file:
    for listitem in value_array_person_one:
        save_file.write('%s\n' % listitem)
#    save_file.write('\n')
with open('excel2.txt', 'w') as save_file:
    for listitem in value_array_person_two:
        save_file.write('%s\n' % listitem)
#    save_file.write('\n')
with open('excel_date.txt', 'w') as save_file:
    for listitem in date_array:
        save_file.write('%s\n' % listitem)