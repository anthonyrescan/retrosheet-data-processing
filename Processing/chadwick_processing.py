import os
import itertools
import shutil
import subprocess
from os import listdir
from os.path import isfile, join

directory = os.path.dirname(__file__)
print(directory)
processing = os.path.join(directory, 'Processing')
processed = os.path.join(directory, 'Processed')
output_location = os.path.join(directory, 'Output')

def process_event(year):
    eventfiles = []
    for filename in os.listdir(processing):
        if filename.endswith(".EVA") or filename.endswith(".EVN") or filename.endswith(".EVE"):
            eventfiles.append(filename)
        else:
            continue
    file = eventfiles[0]
    output_file_info = (file[0:-4]+'_info.csv')
    output_file_home_lineup = (file[0:-4]+'_home_lineup.csv')
    output_file_visitor_lineup = (file[0:-4]+'_visitor_lineup.csv')
    output_file_play = (file[0:-4]+'_play.csv')
    output_file_sub = (file[0:-4]+'_sub.csv')
    #bash_info = 'cwgame -f 0,7,8,9,1,2,4,6,5,12,13,14,24,25,19,26,27,28,29,30,31,32,18,42,43,44 -n -y '+year+' '+file+' > '+output_file_info
    #bash_lineup_home = 'cwgame -f 0,64-81 -n -y '+year+' '+file+' > '+output_file_home_lineup
    #bash_lineup_visitor = 'cwgame -f 0,46-63 -n -y '+year+' '+file+' > '+output_file_visitor_lineup
    #bash_play = 'cwevent -f 0, 96, 2, 3, 10, 5, 6, 7, 29 -n -y '+year+' '+file+' > '+output_file_play
    #bash_sub = 'cwsub -f 0,9,7,2,5,8 -n -y '+year+' '+file+' > '+output_file_sub
    #output_info = subprocess.run(bash_info,shell=True,check=True)
    #output_lineup_home = subprocess.run(bash_lineup_home,shell=True,check=True)
    #output_lineup_visitor = subprocess.run(bash_lineup_visitor,shell=True,check=True)
    #output_play = subprocess.run(bash_play,shell=True,check=True)
    #output_sub = subprocess.run(bash_sub,shell=True,check=True)
    subprocess.run('cd '+processing,shell=True,check=True)
    try:
        subprocess.run('cwgame -f 0,7,8,9,1,2,4,6,5,12,13,14,24,25,19,26,27,28,29,30,31,32,18,42,43,44 -n -y '+year+' '+file+' > '+output_file_info,shell=True,check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    try:
        subprocess.run('cwgame -f 0,64-81 -n -y '+year+' '+file+' > '+output_file_home_lineup,shell=True,check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    try:
        subprocess.run('cwgame -f 0,46-63 -n -y '+year+' '+file+' > '+output_file_visitor_lineup,shell=True,check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    try:
        subprocess.run('cwevent -f 0, 96, 2, 3, 10, 5, 6, 7, 29 -n -y '+year+' '+file+' > '+output_file_play,shell=True,check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    try:
        subprocess.run('cwsub -f 0,9,7,2,5,8 -n -y '+year+' '+file+' > '+output_file_sub,shell=True,check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    shutil.move(processing+file,processed+file)
    shutil.move(processing+output_file_info,output_location+output_file_info)
    shutil.move(processing+output_file_home_lineup,output_location+output_file_home_lineup)
    shutil.move(processing+output_file_visitor_lineup,output_location+output_file_visitor_lineup)
    shutil.move(processing+output_file_sub,output_location+output_file_sub)


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