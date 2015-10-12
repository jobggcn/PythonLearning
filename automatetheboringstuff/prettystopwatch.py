#Exercise 1 Chapter 15 
#Prettified Stopwatch 

import time, pyperclip 

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit') 
input()  #press enter to begin 
print('Started') 
start_time = time.time() 
lap_times = [] 
total_times = []
last_time = start_time 

try: 
    while True: 
        input() 
        lap_times.append(round(time.time() - last_time, 2)) 
        total_times.append(round(time.time() - start_time, 2)) 
        last_time = time.time() #reset the last lap time
        print('Logged time #{}'.format(len(lap_times))) 

except KeyboardInterrupt: 
    #Handle the Ctrl-C exception to keep its error message from displaying
    print('Done') 

output = "" 
for lap in range(len(lap_times)): 
    lap_time = str(lap_times[lap]).rjust(4) 
    total_time = str(total_times[lap]).rjust(5) 
    lap_number = str(lap).rjust(2) 
    output += 'Lap #{}: {} ({})\n'.format(lap_number,total_time,lap_time) 

print(output) 
pyperclip.copy(output) 
