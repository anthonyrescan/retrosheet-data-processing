import os
import itertools
import shutil
import subprocess
from os import listdir
from os.path import isfile, join

directory = r'C:/Users/antho/Documents/Repos/chadwick/'
processed_location = 'C:/Users/antho/Documents/Repos/chadwick/Processed/'
output_location = 'C:/Users/antho/Documents/Repos/chadwick/Output/'

def process_event(year):
    eventfiles = []
    for filename in os.listdir(directory):
        if filename.endswith(".EVA") or filename.endswith(".EVN") or filename.endswith(".EVE"):
            eventfiles.append(filename)
        else:
            continue
    file = eventfiles[0]
    info_output_file = (file[0:-4]+'.csv')
    home_lineup_output_file = (file[0:-4]+'.csv')
    visitor_lineup_output_file = (file[0:-4]+'.csv')
    sub_output_file = (file[0:-4]+'.csv')
    bash_info = 'cwgame -f 0, 7, 8, 9, 1, 2, 4, 6, 5, 12, 13, 14, 24, 25, 19, 26, 27, 28, 29, 30, 31, 32,18,42,43,44 -y '+year+' '+file+' > '+file[0:-4]+'_info.csv'
    bash_lineup_home = 'cwgame -f 0,64-81 -y '+year+' '+file+' > '+info_output_file
    bash_lineup_visitor = 'cwgame -f 0,46-63 -y '+year+' '+file+' > '+home_lineup_output_file
    bash_play = 'cwevent -f 0, 96, 2, 3, 10, 5, 6, 7, 29 -y '+year+' '+file+' > '+visitor_lineup_output_file
    bash_sub = 'cwsub -y '+year+' '+file+' > '+sub_output_file
    output = subprocess.run(bash_command,shell=True,check=True)
    shutil.move(directory+file,processed_location+file)
    shutil.move(directory+output_file,output_location+info_output_file)
    shutil.move(directory+output_file,output_location+home_lineup_output_file)
    shutil.move(directory+output_file,output_location+visitor_lineup_output_file)
    shutil.move(directory+output_file,output_location+sub_output_file)


file_count = []
for filename in os.listdir(directory):
    if filename.endswith(".EVA") or filename.endswith(".EVN") or filename.endswith(".EVE"):
        file_count.append(filename)
    else:
        continue

def repeat(func,n):
    if n > 0:
        for i in range(n):
            func()
    else:
        print("Event Files Processed")

repeat(process_event('2020'),len(file_count))