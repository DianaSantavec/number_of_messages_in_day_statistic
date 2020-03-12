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
    #print (participants['name'])


#set last day
timestamp= int (data['messages'][0]['timestamp_ms'])
full_prew_date = date.fromtimestamp(timestamp/1000.0)
prew_message_day = full_prew_date.day

#get first day
counter = len(data['messages'])
timestamp = int (data['messages'][counter-1]['timestamp_ms'])
full_first_day = date.fromtimestamp(timestamp/1000.0)
first_message_dat = full_first_day.day


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
        value_array_person_one.append(number_of_messages[0])
        value_array_person_two.append(number_of_messages[1])

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

value_array_person_one.append(number_of_messages[0])
value_array_person_two.append(number_of_messages[1])

#X pravi brojeve za svaki datum da bi se moglo odrediti rastojanje izmedju stubica
X = np.arange(len(date_array))
fig,ax = plt.subplots()
rects1 = ax.bar(X-0.25/2, value_array_person_one,0.25,label = names[0])
rects1 = ax.bar(X+0.25/2, value_array_person_two,0.25,label = names[1])

ax.set_ylabel('Number of messages')
ax.set_title('message analysis')
ax.set_xticks(X)
ax.set_xticklabels(date_array)
ax.legend()
plt.show()

#fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#ax = plt.subplot(111)
#ax.bar(date_array, value_array_person_one, color = 'b', width = 0.25)
#ax.bar(date_array, value_array_person_two, color = 'g', width = 0.25)
##ax.xaxis_date()
#plt.show()



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
