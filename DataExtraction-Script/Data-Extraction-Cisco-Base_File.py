## Import Necessary Library
import os
import sys
import re
import datetime
import glob
import csv


## Define file name
ddt = str(datetime.datetime.now().strftime("%d-%m-%y--%H-%M-%M"))
currentMonth = str(datetime.datetime.now().strftime('%B-%Y'))
output_files = "Extract_Data"+'-'+currentMonth+'_'+'Timestamp-'+ddt+'.csv'
name = str(output_files)
print("Extracted File Name : ", name)
print(currentMonth)

## Define & Check File Path to Source File
path = os.getcwd()
print ("File Path : ",path)

## Open Multiple File 
# Change the source file pattern to match file name pattern, you may remove '[WSA]' with suitable pattern file
source_file = glob.glob(os.path.join(path,"[WSA]*.txt"))
print ("Source File Name : ",source_file)

for file in source_file:
 files = open(file,'r')
 line_re = files.read()
 
 ## Begin Data Extraction for specific information using defined regex
 # Change this line below with your defined regex, you may add more regex to this line
 hostname = re.findall('hostname.*', line_re)
 hostname2 = re.findall('WSA2[-]\w*[#]|WSA2[-]\w*[-#]\w*[-#12]\w*[-#]\w*', line_re)
 cpu_ios_xe = re.findall('five minutes\: \d*\%', line_re)
 cpu_ios = re.findall('[;].five.minutes\:.\d*\%', line_re)
 cpu_ios_1 = re.findall('[;] five minutes: \d*%', line_re)
 process_memory = re.findall('Processor.Pool.Total:..\d*.Used:..\d*.Free:..\d*', line_re)
 process_memory_xe = re.findall('System.memory..:.\d*K.total,.\d*K.used,.\d*K.free,.\d*K.kernel.reserved', line_re)
 process_memory_94K = re.findall('System.memory:.\d*K.total,.\d*K.used,.\d*K.free',line_re)
 cpu_asa = re.findall('[;].5.minutes:.\d*%', line_re)
 memory_asa = re.findall('.bytes.[(](.|..\d*%.)[)]', line_re)
 memory_asa2 = re.findall('Used memory:........\d*.bytes.[(]\d*%[)]', line_re)
 cpu_nx = re.findall('CPU states  :...\d*[.]\d*% user[,]...\d*[.]\d*% kernel[,]...\d*[.]\d*% idle', line_re)
 memory_nx = re.findall('Memory usage:...\d*K total[,]...\d*K used[,]...\d*K free', line_re)
 
 ## For Debug Purpose please uncomment below line \/,
 # and comment the Extract Data line code to prevent from save unnecessary data, add more 
 #print(hostname)
 #print(cpu_ios)
 #print(cpu_ios_xe)
 #print(process_memory)
 
 ## Extract Data and write it to CSV File
 # Comment this line below when enable Debug Line
 with open(name, 'a') as csvfile:
      filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
      filewriter.writerow(hostname)
      filewriter.writerow(hostname2)
      filewriter.writerow(cpu_ios_xe)
      filewriter.writerow(cpu_ios)
      filewriter.writerow(cpu_ios_1)
      filewriter.writerow(process_memory)
      filewriter.writerow(process_memory_xe)
      filewriter.writerow(process_memory_94K)
      filewriter.writerow(cpu_asa)
      filewriter.writerow(memory_asa)
      filewriter.writerow(memory_asa2)
      filewriter.writerow(cpu_nx)
      filewriter.writerow(memory_nx)
