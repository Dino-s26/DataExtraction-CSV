## Import Necessary Library
import os
import sys
import re
import datetime
import glob
import csv
import errno

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
# Change the source file pattern to match file name pattern
source_file = glob.glob(os.path.join(path,"[WSAMBCAWSBY]*.txt"))
print ("Source File Name : ",source_file)

for file in source_file:
 files = open(file,'r')
 line_re = files.read()
 
 # Begin Data Extraction for specific information using defined regex
 hostname = re.findall('hostname.*', line_re)
 hostname2 = re.findall('WSA2[-]\w*[#]|WSA2[-]\w*[-#]\w*[-#12]\w*[-#]\w*', line_re)
 conn = re.findall('Conns *\d* *\d* *\d* *\d* \w* *\d* \w.*', line_re)

 
 # For Debug Purpose please uncomment below line \/,
 # and comment the Extract Data line code to prevent from save unnecessary data
 #print(hostname)
 #print(cpu_ios)
 #print(cpu_ios_xe)
 #print(process_memory)
 #print(process_memory_xe)
 #print(cpu_asa)
 #print(memory_asa)
 
 # Extract Data and write it to CSV File
 with open(name, 'a') as csvfile:
      filewriter = csv.writer(csvfile,quotechar='|',quoting=csv.QUOTE_MINIMAL)
      filewriter.writerow(hostname)
      filewriter.writerow(hostname2)
      filewriter.writerow(conn)
      